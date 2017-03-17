class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s) + 1
        dp = [False] * size
        dp[0] = True
        for i in range(1, size):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
