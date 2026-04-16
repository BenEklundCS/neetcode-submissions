class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                r = int(stack.pop())
                l = int(stack.pop())
                if token == '+':
                    stack.append(l + r)
                elif token == '-':
                    stack.append(l - r)
                elif token == '*':
                    stack.append(l * r)
                else:
                    stack.append(l / r)
            else:
                stack.append(token)
        return int(stack[-1])
            