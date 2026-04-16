class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                top = stack.pop()
                if (top is '(' and c is not ')') or (top is '[' and c is not ']') or (top is '{' and c is not '}'):
                    return False
        return True if len(stack) == 0 else False