class NumArray:

    def __init__(self, nums: List[int]):
        # Ek prefix sum array banayein jismein starting mein 0 ho
        # Isse indices handle karna aasan ho jata hai
        self.prefix_sums = [0] * (len(nums) + 1)
        
        # Har element ka cumulative sum store karein
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Range sum nikalne ke liye: prefix_sums[right + 1] - prefix_sums[left]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)