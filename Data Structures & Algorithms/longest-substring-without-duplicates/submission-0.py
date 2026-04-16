class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        a = 0

        m = {}
        longest = 0

        while a < len(s):
            b = a
            length = 0
            while b < len(s) and s[b] not in m:
                m[s[b]] = 1
                length += 1
                b += 1
            m = {}
            a += 1
            if length > longest:
                longest = length
        return longest
        
            