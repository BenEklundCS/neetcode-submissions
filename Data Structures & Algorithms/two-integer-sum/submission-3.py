class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if n in m:
                return [m[n], i]
            else:
                m[target - n] = i
         