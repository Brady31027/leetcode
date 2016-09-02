# https://fxrcode.gitbooks.io/leetcodenotebook/content/Leetcode_Medium/best_time_to_buy_and_sell_stock_with_cooldown.html
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #define three states:
        # s0: owner has no stock and can buy one immediatly
        # s1: owner has a stock
        # s2: owner just sold a stock but can't buy one immediatly
        # --- [DP] ---
        # s0[i] = max(s0[i-1], s2[i-1]) 
        # s1[i] = max(s1[i-1], s0[i-1] - price[i])
        # s2[i] = s1[i-1] + price[i]
        # init(s0) = 0
        # init(s1) = -price[0]
        # init(s2) = NAN /*cannot sell before buy*/
        if len(prices) < 2: return 0
        l_s0, l_s1, l_s2 = [0]*2, [0]*2, [0]*2
        l_s0[0], l_s1[0], l_s2[0] = 0, -prices[0], -99999
        for i in range(1, len(prices)):
            l_s0[i%2] = max(l_s0[(i-1)%2], l_s2[(i-1)%2])
            l_s1[i%2] = max(l_s1[(i-1)%2], l_s0[(i-1)%2] - prices[i])
            l_s2[i%2] = l_s1[(i-1)%2] + prices[i]
        return max(l_s0[(len(prices)-1)%2], l_s2[(len(prices)-1)%2])
