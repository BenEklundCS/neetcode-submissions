class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minSize = float('infinity')

        currentSum = 0
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                minSize = min(minSize, r - l + 1)
                currentSum -= nums[l]
                l += 1
            
        return minSize if minSize != float('infinity') else 0