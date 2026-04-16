class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                right = int(stack.pop())
                left = int(stack.pop())

                evaluation = 0

                match token:
                    case '+':
                        evaluation = left + right
                    case '-':
                        evaluation = left - right
                    case '*':
                        evaluation = left * right
                    case '/':
                        evaluation = left / right
                stack.append(evaluation)
            else:
                stack.append(token) # add numbers to the stack

        return int(stack[-1])