class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # MEMORIZE THIS ALGORITHM

        # Define low and high on the array, these are simply both ENDS of the array for now
        low = 0
        high = len(nums) - 1
        # GET THE MIDDLE OF THE ARRAY BY TAKING THE AVERAGE OF LOW AND HIGH
        mid = int((low + high)/2)

        # ITERATE WHILE LOW <= HIGH because it is only when low > high that we return -1, NOT low == high
        while low <= high:
            # MAIN ALGORITHM:
                # Check if mid is at target
                if nums[mid] == target:
                    return mid
                # If not, check if target is greater than mid
                    # If so, we shrink the array to the right side (SEARCH GREATER VALUES)
                elif nums[mid] < target:
                    low = mid + 1
                # Otherwise, check if target is less than mid
                    # If so, we shrink the array to the left side (SEARCH SMALLER VALUES)
                else:
                    high = mid - 1
                # RECALCULATE MID
                mid = int((low + high)/2)
        # RETURN -1 IF NOT FOUND
        return -1
