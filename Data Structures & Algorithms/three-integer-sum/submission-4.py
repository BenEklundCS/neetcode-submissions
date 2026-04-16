class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result initialization
        res = []
        # sort the input array, this will allow me to use a two-ptr approach
        nums.sort()
        # iterate over the sorted array
        for i, v in enumerate(nums):
            # if we've already tried the current i value, move on:
            if i > 0 and v == nums[i - 1]:
                continue
            # pick the inverse of the value as our target
            target = -v
            # find two numbers such that they add up to target, using two-ptr approach

            # define the pointers prior to the loop
            l = i + 1 # why?
            # l != 0, because we do not want to check values at indexes < i because they will have been already picked up (avoid duplicates!)
            r = len(nums) - 1 # right ptr always points to the end of the array
            while l < r: # not <= because these indices should never be equal (avoid duplicates!)
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # move ptrs
                    l += 1
                    r -= 1
                    # move l forward until it's no longer equal
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else: 
                    l += 1
        return res
                

