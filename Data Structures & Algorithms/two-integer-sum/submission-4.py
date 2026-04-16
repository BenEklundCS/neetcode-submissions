class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}

        for i, num in enumerate(nums):
            result = target - num
            if result not in results:
                results[num] = i
            else:
                return [results[result], i]

        print(results)

        
        



