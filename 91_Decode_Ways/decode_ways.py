class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0 or s[0] == "0": return 0
        dp = [1 for _ in range(size+1)]    
        for i in range(2, size+1):
            if (10 <= int(s[i-2: i]) <= 26) and s[i-1] != '0':
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-2: i] == '10' or s[i-2: i] == '20':
                dp[i] = dp[i-2]
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[-1]
