class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Build a set for O(1) lookup time and rm duplicates
        num_set = set(nums)
        # Longest is set to 0 at the algo start
        longest = 0

        # Iterate over the set
        for n in num_set:
            # We found a new start of a set if n - 1 isn't already in the set
            if n - 1 not in num_set: 
                # Once a new start is found, we want to measure that sequences length
                length = 0
                # Move forward and increment the length as long as n + length is in the set
                while n + length in num_set:
                    length += 1
                # Now we check if it beat the previous longest value
                if length > longest:
                    longest = length
        # At this point the longest sequence is always found
        return longest
                
