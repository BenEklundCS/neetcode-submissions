class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if I make no transactions maxProfit is 0
        maxProfit = 0
        buyPrice = prices[0]

        for price in prices:
            profit = price - buyPrice
            maxProfit = max(profit, maxProfit)
            buyPrice = min(price, buyPrice)
        
        return maxProfit