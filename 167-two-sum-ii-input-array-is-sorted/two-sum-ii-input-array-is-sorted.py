class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Do pointers initialize karein: ek start mein aur ek end mein
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # 1-indexed array return karna hai isliye +1 kiya
                return [left + 1, right + 1]
            elif current_sum < target:
                # Agar sum chota hai, toh left pointer ko aage badhayein
                left += 1
            else:
                # Agar sum bada hai, toh right pointer ko peeche layein
                right -= 1