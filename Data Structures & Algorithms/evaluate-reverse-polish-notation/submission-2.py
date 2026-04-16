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
                if token == '+': # add
                    res = l + r
                elif token == '-': # subtract
                    res = l - r
                elif token == '*': # multiply
                    res = l * r
                else: # divide
                    res = l / r
                stack.append(res) 
            else:
                stack.append(token)
        return int(stack[-1])
