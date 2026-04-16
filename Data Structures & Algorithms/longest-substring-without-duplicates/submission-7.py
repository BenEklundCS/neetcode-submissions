class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        start = 0
        longest = 0

        for end, char in enumerate(s):
            # char is a duplicate at right boundary
            # AND is within the current window
            if char in hashMap and hashMap[char] >= start:
                start = hashMap[char] + 1 # move start to the right of the last occurance
            hashMap[char] = end
            longest = max(longest, end - start + 1)
        return longest