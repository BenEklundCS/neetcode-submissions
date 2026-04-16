class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = [0] * (n + 1) # make lst len(n) + 1 long
        
        for i in range(1, n + 1):
            lst[i] = lst[i >> 1] + (i & 1)
        return lst