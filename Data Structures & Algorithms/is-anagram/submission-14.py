class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def getAlphabetPos(c):
            return ord(c) - ord('a')

        count = [0] * 26

        for i in range(len(s)):
            posS = getAlphabetPos(s[i])
            posT = getAlphabetPos(t[i])
            count[posS] += 1
            count[posT] -= 1

        for i in count:
            if i != 0:
                return False
        return True
