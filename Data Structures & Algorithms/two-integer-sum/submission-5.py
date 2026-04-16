class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            cousin = target - num
            if cousin in hashMap:
                cousinIndex = hashMap[cousin]
                return [cousinIndex, index]
            else:
                hashMap[num] = index
         

