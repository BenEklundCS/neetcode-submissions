class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # notes:
        # two obvious solutions, both are discouraged
        # 1. modify the input array. If we sort the array, we can then do an O(n) pass to find the dup
        # 2. use a hashmap w/ O(n) extra space, and if a key collision occurs return the key

        # goal: find a solution that does not require modifying nums, OR more than O(1) extra space
        
        seen = [0] * len(nums)
        for n in nums:
            if seen[n] == -1:
                return n
            seen[n] = -1
        
        