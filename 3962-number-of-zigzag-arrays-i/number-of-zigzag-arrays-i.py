class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        if m <= 0:
            return 0
        
        # dp0[j] -> valid arrays ending at j where the last move was DOWN (next must be UP)
        # dp1[j] -> valid arrays ending at j where the last move was UP (next must be DOWN)
        dp0 = [1] * m
        dp1 = [1] * m
        
        for _ in range(2, n + 1):
            next_dp0 = [0] * m
            next_dp1 = [0] * m
            
            # For next_dp1[j] (last move UP), previous element must be strictly less than j
            pref0 = 0
            for j in range(m):
                next_dp1[j] = pref0
                pref0 = (pref0 + dp0[j]) % MOD
                
            # For next_dp0[j] (last move DOWN), previous element must be strictly greater than j
            suff1 = 0
            for j in range(m - 1, -1, -1):
                next_dp0[j] = suff1
                suff1 = (suff1 + dp1[j]) % MOD
                
            dp0, dp1 = next_dp0, next_dp1
            
        return (sum(dp0) + sum(dp1)) % MOD