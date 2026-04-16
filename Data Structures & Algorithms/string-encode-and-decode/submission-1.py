class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '%' + s
        return encoded_string
            

    def decode(self, s: str) -> list[str]:
        decoded_list = []
        index = 0
        while index < len(s):
            # get the length to read past the %
            str_length = ""
            while s[index] != '%':
                str_length += s[index]
                index += 1
            # Convert str_length to a number
            length = int(str_length)
            # advance index past the delimiter '%'
            index += 1
            decoded_list.append(s[index : index + length])
            # advance index to the end of the current string
            index = index + length
        return decoded_list
