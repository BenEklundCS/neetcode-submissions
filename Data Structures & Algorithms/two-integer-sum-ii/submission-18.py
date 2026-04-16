class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) < 2:
            raise Exception("Array too short!")

        # Two-pointer algorithm
        low = 0
        high = len(numbers) - 1

        s = numbers[low] + numbers[high]

        # Once s is target we've found the two numbers
        while s != target:
            if s > target:
                high -= 1
            elif s < target:
                low += 1
            s = numbers[low] + numbers[high]
        
        # Found
        return [low + 1, high + 1]

        
