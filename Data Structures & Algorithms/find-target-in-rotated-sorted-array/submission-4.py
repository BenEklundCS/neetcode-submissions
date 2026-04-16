class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # which portion of the array are we in?
            
            if nums[l] <= nums[mid]: # left sorted portion
                if target > nums[mid] or target < nums[l]: # search right
                    l = mid + 1
                else:
                    r = mid - 1


            else: # right sorted portion
                if target < nums[mid] or target > nums[r]: # search left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1