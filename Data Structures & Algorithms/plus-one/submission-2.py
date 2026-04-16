class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        # Find where the 1 will fit
        while i > 0 and digits[i] + 1 >= 10:
            digits[i] = 0
            i -= 1
        
        # If it fits, add it and return
        if digits[i] + 1 < 10:
            digits[i] += 1
            return digits
        else:
            # Return 1 + 000...000 
            return [1] + [0] * len(digits)