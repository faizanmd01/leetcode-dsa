class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the last seen index of 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_seen[char] = i
            # If all characters have been seen at least once
            if -1 not in last_seen.values():
                # The number of valid substrings ending at index i
                # is equal to 1 + the minimum index among 'a', 'b', and 'c'
                count += 1 + min(last_seen.values())
                
        return count