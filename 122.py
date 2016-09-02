class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        gain = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0: gain += (prices[i] - prices[i-1])
        return gain
