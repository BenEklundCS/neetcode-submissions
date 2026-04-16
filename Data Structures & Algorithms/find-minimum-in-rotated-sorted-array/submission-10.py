class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set up binary search pointers
        low = 0
        high = len(nums) - 1

        # Continue while low < high, move them closer together towards the result
        while low < high:
            mid = int((low + high) / 2)
            # lowest value must be to the right of mid
            if nums[mid] > nums[high]:
                low = mid + 1
            # otherwise lowest value must be to the left of mid
            else:
                high = mid
        return nums[low]







