class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # Push open parens
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                o = stack.pop()
                print(c, o)
                invalid_paren = (c == ')' and o != '(')
                invalid_curly = (c == '}' and o != '{')
                invalid_square = (c == ']' and o != '[')
                if invalid_paren or invalid_curly or invalid_square:
                   return False
        return True if len(stack) == 0 else False