class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # try without o(1) space first
        hashMap = {}
        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        return max(hashMap, key=hashMap.get)
