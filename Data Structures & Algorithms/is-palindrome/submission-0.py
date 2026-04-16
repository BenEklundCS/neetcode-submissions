class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        l = 0
        r = len(s) - 1

        while l < len(s):
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
            