class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_price # if we sell now, what do we get?
            max_profit = max(profit, max_profit) # update max if max
            min_price = min(price, min_price) # update min if min
        return max_profit 
