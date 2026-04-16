class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            # if token is a math operator do math
            if token in operators:
                # math
                r = int(stack.pop())
                l = int(stack.pop())
                res = 0
                # add
                if token == '+':
                    res = l + r
                elif token == '-':
                    res = l - r
                elif token == '*':
                    res = l * r
                else:
                    res = l / r
                stack.append(res) 
            else:
                stack.append(token)
        return int(stack[-1])
