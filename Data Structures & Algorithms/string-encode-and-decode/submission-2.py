class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s))+"/"+s)
        return ''.join(encoded_str)


    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            # read the number
            length = []
            while s[i] != "/":
                length.append(s[i])
                i += 1
            length_to_read = int(''.join(length))

            # move past the delimiter
            i += 1

            res.append(s[i: i + length_to_read])
            # advance index to the end of the current string
            i = i + length_to_read
        return res





