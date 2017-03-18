class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10: n = 10
        dp = [1]+ [9] * n
        for i in range(2, n + 1):
            for j in range(9, 9-i+1, -1):
                dp[i] *= j
        return sum(dp)
