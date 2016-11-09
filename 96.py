class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        elif n == 1: return 1
        elif n == 2: return 2
        l_dp = [0 for i in xrange(n+1)]
        l_dp[0], l_dp[1], l_dp[2] = 1, 1, 2
        for i in xrange(3, n+1):
            for j in xrange(1, i+1):
                l_dp[i] += l_dp[j-1] * l_dp[i-j]
        return l_dp[n]
                
