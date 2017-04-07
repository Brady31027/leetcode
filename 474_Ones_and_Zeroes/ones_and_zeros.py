class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            consuming_zeros, consuming_ones = s.count('0'), s.count('1')
            for z in range(m, consuming_zeros - 1, -1):
                for o in range(n, consuming_ones - 1, -1):
                    dp[z][o] = max(dp[z - consuming_zeros][o - consuming_ones] + 1, dp[z][o])
        return dp[-1][-1]
