class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = int((high + low)/2)
        
        while low <= high:
            # Found
            if nums[mid] == target:
                return mid
            # Too high
            elif nums[mid] > target:
                high = mid - 1
            # Too low
            else:
                low = mid + 1
            mid = int((high + low)/2)
        return -1