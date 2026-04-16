class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(chosen, remaining):
            # base case
            res.append(chosen[:]) # append a copy of chosen
            # recursive step
            for i in range(len(remaining)):
                chosen.append(remaining[i])
                backtrack(chosen, remaining[i+1:])
                chosen.pop()
        backtrack([], nums)
        return res
        