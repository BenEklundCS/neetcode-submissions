class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []

        def count(n: int) -> int:
            res = 0
            for i in range(32):
                if (1 << i) & n:
                    res += 1
            return res
        
        for i in range(n + 1):
            lst.append(count(i))
        return lst