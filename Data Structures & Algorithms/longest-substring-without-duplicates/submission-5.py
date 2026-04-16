class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character
        m = {}
        # Initialize pointers and the result
        start = 0
        longest = 0

        for end in range(len(s)):
            # If character is already in the map and is within the current window
            if s[end] in m and m[s[end]] >= start:
                # Move the start pointer to the right of the last occurrence
                start = m[s[end]] + 1
            # Update the character's last index
            m[s[end]] = end
            # Update the longest substring length
            longest = max(longest, end - start + 1)
        
        return longest
        
            