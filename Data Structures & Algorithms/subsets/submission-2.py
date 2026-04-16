class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(chosen, remaining):
            # base case
            subsets.append(chosen[:])

            # recursive step
            for i in range(len(remaining)):
                print(chosen)
                chosen.append(remaining[i])
                backtrack(chosen, remaining[i+1:])
                chosen.pop()

        backtrack([], nums)
        return subsets