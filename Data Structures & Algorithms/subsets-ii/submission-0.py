class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort nums to avoid duplicates

        subsets = []

        def backtrack(chosen, remaining):
            if chosen not in subsets:
                subsets.append(chosen[:])
            for i in range(len(remaining)):
                chosen.append(remaining[i])
                backtrack(chosen, remaining[i+1:])
                chosen.pop()
        backtrack([], nums)
        return subsets