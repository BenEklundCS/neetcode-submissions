class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0
        for n in nums:
            if n == 0:
                maxCount = max(currentCount, maxCount)
                currentCount = 0
            else:
                currentCount += 1
        maxCount = max(currentCount, maxCount)
        return maxCount
