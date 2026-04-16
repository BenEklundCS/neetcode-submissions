class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))+"/"+s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            str_length = []
            while s[i] != "/":
                str_length.append(s[i])
                i += 1
            i += 1 # move past the delimiter
            
            word = []
            str_length = int(''.join(str_length))
            while str_length > 0:
                word.append(s[i])
                i += 1
                str_length -= 1
            res.append(''.join(word))
        return res



