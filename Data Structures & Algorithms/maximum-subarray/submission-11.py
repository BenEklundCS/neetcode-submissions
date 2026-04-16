class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        prefix = 0
        for n in nums:
            if prefix < 0:
                prefix = 0
            prefix += n
            max_sum = max(prefix, max_sum)
        return max_sum