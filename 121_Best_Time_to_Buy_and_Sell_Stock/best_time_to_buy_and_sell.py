class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        minPrice, maxProfit = prices[0], 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
