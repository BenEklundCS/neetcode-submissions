class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # backtracking theory
        # 1. add an element to the current solution
        # 2. recursively backtrack with it added
        # 3. remove the element
        result = []
        def backtrack(current, remaining):
            result.append(current[:])
            # Backtracking base case
            # Backtracking recursive step
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[i + 1:])
                current.pop()
            return current
        backtrack([], nums)
        return result