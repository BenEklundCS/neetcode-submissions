class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if we do it backwards there's an easy greedy algo
        ptr = len(nums) - 1
        last = ptr
        while ptr >= 0:
            if nums[ptr] + ptr >= last:
                last = ptr
            ptr -= 1
        return last == 0
