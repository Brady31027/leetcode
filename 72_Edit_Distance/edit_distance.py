class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size_src, size_dst = len(word1)+1, len(word2)+1
        dp = [[ 0 for _ in range(size_src) ] for _ in range(size_dst)]
        for i in range(1,size_src): dp[0][i] = dp[0][i-1] + 1 # go right
        for i in range(1,size_dst): dp[i][0] = dp[i-1][0] + 1 # go down
        for i in range(1, size_dst):
            for j in range(1, size_src):
                insertion = dp[i-1][j] + 1
                deletion = dp[i][j-1] + 1
                replacement =  0 if word1[j-1] == word2[i-1] else 1
                replacement = dp[i-1][j-1] + replacement
                dp[i][j] = min(insertion, deletion, replacement)
        return dp[-1][-1]
