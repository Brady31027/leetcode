class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1)+1, len(word2)+1
        ll_dist = [[0 for x in xrange(n)] for y in xrange(m)]
        for x in xrange(n): ll_dist[0][x] = x
        for y in xrange(m): ll_dist[y][0] = y
        for y in xrange(1, m):
            for x in xrange(1, n):
                ll_dist[y][x] = min(ll_dist[y-1][x]+1, ll_dist[y][x-1]+1, ll_dist[y-1][x-1]+(0 if word1[y-1] == word2[x-1] else 1))
        return ll_dist[m-1][n-1]
        
