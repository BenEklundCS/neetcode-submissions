class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, remaining):
            # base case
            result.append(current[:]) 
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[i + 1:])
                current.pop()

        backtrack([], nums)
        return result
