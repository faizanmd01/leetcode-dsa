class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        current_sum=0

        prefix_sums={0:1}

        for num in nums:
            current_sum+=num

            if(current_sum-k) in prefix_sums:
                count+=prefix_sums[current_sum-k]

            if current_sum in prefix_sums:
                prefix_sums[current_sum]+=1
            else:
                prefix_sums[current_sum]=1

        return count
        