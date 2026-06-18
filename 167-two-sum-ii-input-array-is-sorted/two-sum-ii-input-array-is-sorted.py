class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Do pointers set karein: ek shuruat mein aur ek aakhiri mein
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # Agar sum target ke barabar mil gaya
            if current_sum == target:
                # 1-indexed answer chahiye, isliye donon mein +1 karenge
                return [left + 1, right + 1]
            
            # Agar sum target se bada hai, toh right pointer ko piche lao
            elif current_sum > target:
                right -= 1
                
            # Agar sum target se chota hai, toh left pointer ko aage badhao
            else:
                left += 1