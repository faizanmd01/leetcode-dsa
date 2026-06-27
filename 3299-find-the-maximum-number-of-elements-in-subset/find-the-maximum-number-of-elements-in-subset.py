from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        # 1. Handle the special case of 1s
        if 1 in count:
            ans = count[1] if count[1] % 2 != 0 else count[1] - 1
            
        # 2. Check chains for numbers > 1
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            # Keep climbing the chain as long as we have at least 2 elements
            while curr in count and count[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            # If the peak element exists at least once, it completes the sequence
            if curr in count:
                current_len += 1
            else:
                # If the peak element doesn't exist, remove 1 from the sides 
                # to turn the last paired element into the peak
                current_len -= 1
                
            ans = max(ans, current_len)
            
        return ans