class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1
                # Condición: target aparece estrictamente más de la mitad de las veces
                if count * 2 > (j - i + 1):
                    ans += 1
        return ans