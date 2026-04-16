class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opening, closing):
            # we have used all parens from n because len str == 2n
            if opening == closing == n:
                res.append("".join(stack))
                return # because we are done with the problem
            
            if opening < n: # explore adding an open paren, which is valid if open < n
                stack.append('(')
                backtrack(opening + 1, closing)
                stack.pop()
            if closing < opening: # only explore closing if its valid to do so (closed must be <= opening for valid parens)
                stack.append(')')
                backtrack(opening, closing + 1)
                stack.pop()

        backtrack(0, 0)
        return res