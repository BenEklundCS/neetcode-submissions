class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(chosen, remaining):
            # base case
            if sum(chosen) == target:
                combinations.append(chosen[:])
            elif sum(chosen) > target:
                chosen = []
            else:
                for i in range(len(remaining)):
                    chosen.append(remaining[i])
                    backtrack(chosen, remaining[i:])
                    chosen.pop()
            
        backtrack([], nums)
        return combinations