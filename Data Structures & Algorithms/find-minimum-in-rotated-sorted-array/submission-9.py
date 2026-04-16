class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Binary search pattern
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = int((high + low) // 2)
            # Lowest value is to the right of mid
            if nums[mid] > nums[high]:
                low = mid + 1
            # Lowest value is to the left of mid
            else:
                high = mid
        return nums[low]