class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking with pruning
        stack = []
        res = []

        def backtrack(openers, closers):
            if openers == closers == n:
                res.append(''.join(stack))
                return
            # explore opener
            if openers < n:
                stack.append('(')
                backtrack(openers + 1, closers)
                stack.pop()
            if closers < openers:
                stack.append(')')
                backtrack(openers, closers + 1)
                stack.pop()

        backtrack(0, 0)
        return res