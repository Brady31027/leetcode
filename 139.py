class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s)
        l_dp = [False] * (size+1)
        l_dp[0] = True
        for i in xrange(size+1):
            for j in xrange(i):
                if l_dp[j] and s[j:i] in wordDict: l_dp[i] = True
        return l_dp[-1]
        
