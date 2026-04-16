class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(current, remaining):
            s = sum(current)
            if s == target:
                result.append(current[:])
            elif s > target:
                current = []
            else:
                for i in range(len(remaining)):
                    current.append(remaining[i])
                    backtrack(current, remaining[i:])
                    current.pop()

        backtrack([], nums)
        return result