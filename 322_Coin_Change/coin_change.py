class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7ffffffe
        dp = [0] + [INF] * amount
        for i in range(amount + 1):
            for c in coins:
                if i + c <= amount:
                    dp[i + c] = min( dp[i] + 1, dp[i+c])
        return dp[amount] if dp[amount] < INF else -1
