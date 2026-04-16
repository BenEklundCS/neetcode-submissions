class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # number at the pile over the eating rate

            if hours <= h:
                res = min(res, k)
                r = k - 1 # rate worked, search for smaller
            else:
                l = k + 1 # rate did not work, search bigger
        return res
