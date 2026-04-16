class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {')' : '(', '}' : '{', ']' : '['}

        def getTop(stack):
            return stack[-1]

        for c in s:
            if c in closeToOpen:
                if stack and getTop(stack) == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False