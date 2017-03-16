class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 1 if n == 0 else n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            for j in range(i):
                dp[i] += (dp[j] * dp[i-j-1])
        return dp[-1]
