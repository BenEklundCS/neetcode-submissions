class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            # If there's a 1 at the location in n determined by 1 << i
            if (1 << i) & n:
                res += 1
        return res
                