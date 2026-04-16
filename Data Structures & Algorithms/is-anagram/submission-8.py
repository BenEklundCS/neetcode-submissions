class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getAlphabetPos(c):
            return ord(c) - ord('a') + 1

        count = [0] * 27

        for c in s:
            pos = getAlphabetPos(c)
            print(pos)
            count[pos] += 1
        for c in t:
            pos = getAlphabetPos(c)
            count[pos] -= 1

        for i in count:
            if i != 0:
                return False

        return True
