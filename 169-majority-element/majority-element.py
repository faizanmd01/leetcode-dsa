class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count reaches 0, we pick the current number as the new candidate
            if count == 0:
                candidate = num
            
            # Increment count if the number matches our candidate, otherwise decrement
            count += 1 if num == candidate else -1
            
        return candidate