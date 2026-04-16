class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1 and n not in seen:
            seen[n] = 1
            # squares_of_digits
            sod = []
            while n:
                digit = n % 10
                sod.append(digit * digit)
                n = n // 10
            n = sum(sod)
        
        return n == 1