class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 0
        
        for num in arr:
            max_val = min(max_val + 1, num)
            
        return max_val