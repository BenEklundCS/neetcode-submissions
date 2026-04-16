class Solution:
    def maxSubArray(self, nums) -> int:
        largest_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            largest_sum = max(curr_sum, largest_sum)
        return largest_sum