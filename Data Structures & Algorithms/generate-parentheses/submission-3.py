class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(op, clo):
            # base case is when we have used all parens in n
            if op == clo == n:
                res.append(''.join(stack))
            # explore adding an open paren to the res
            if op < n:
                stack.append('(')
                backtrack(op + 1, clo)
                stack.pop()
            if clo < op:
                stack.append(')')
                backtrack(op, clo + 1)
                stack.pop()

        backtrack(0, 0)
        return res