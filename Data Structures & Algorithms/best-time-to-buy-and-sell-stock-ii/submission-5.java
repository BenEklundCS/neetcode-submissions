class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buyPrice = 0;
        boolean stockHeld = false;

        for (int i = 0; i < prices.length - 1; i++) {
            // sell when next price is < curr price and we're holding
            // buy when stock not held and curr price < next price
            if (stockHeld && prices[i + 1] < prices[i]) {
                maxProfit += prices[i] - buyPrice;
                stockHeld = false;
            }
            if (!stockHeld && prices[i + 1] > prices[i]) {
                buyPrice = prices[i];
                stockHeld = true;
            }
        }

        if (stockHeld) {
            maxProfit += prices[prices.length - 1] - buyPrice;
        }

        return maxProfit;
    }
}