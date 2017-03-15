class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t): return 0
        elif len(s) == len(t) and s != t: return 0
        dp = [[0 for _ in range(len(s) + 1) ] for _ in range(len(t) + 1) ]
        for i in range(len(s)+1): dp[0][i] = 1
        for y in range(1, len(t)+1):
            for x in range(1, len(s)+1):
                if s[x-1] == t[y-1]:
                    dp[y][x] = dp[y][x-1] + dp[y-1][x-1]
                else:
                    dp[y][x] = dp[y][x-1]
        return dp[-1][-1]
