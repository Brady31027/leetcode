class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size < 3:
            if size < 2: return 0
            else: return max(0, prices[1] - prices[0])
        sell = [0] + [None] * (size - 1)
        buy = [-prices[0]] + [None] * (size - 1)
        for i in range(1, size):
            diff = prices[i] - prices[i-1]
            buy[i] = max((sell[i-2] - prices[i]) if i > 1 else None, buy[i-1] - diff)
            sell[i] = max(buy[i-1] + prices[i], sell[i-1] + diff)
        return max(sell)
