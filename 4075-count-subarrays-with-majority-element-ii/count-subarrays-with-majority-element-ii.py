from collections import defaultdict

class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return 0
            
        counts = defaultdict(int)
        counts[0] = 1  # Base case for prefix balance
        
        balance = 0
        ans = 0
        valid_prefixes = 0
        
        for x in nums:
            if x == target:
                # Balance increases: all previous prefixes with 'balance' now become valid,
                # plus we add the count of the balance we just stepped over.
                valid_prefixes += counts[balance]
                balance += 1
            else:
                # Balance decreases: previous prefixes at the new balance are no longer valid.
                balance -= 1
                valid_prefixes -= counts[balance]
                
            ans += valid_prefixes
            counts[balance] += 1
            
        return ans