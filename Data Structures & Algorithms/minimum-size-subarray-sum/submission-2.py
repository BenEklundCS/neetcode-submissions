class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, currentSum = 0, 0
        minLength = float('infinity')

        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                minLength = min(minLength, r - l + 1)
                currentSum -= nums[l]
                l += 1

        return minLength if minLength != float('infinity') else 0