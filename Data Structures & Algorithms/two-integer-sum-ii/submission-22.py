class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            this_sum = numbers[left] + numbers[right]
            if this_sum == target:
                return [left + 1, right + 1]
            elif this_sum < target:
                left += 1
            else:
                right -= 1
        