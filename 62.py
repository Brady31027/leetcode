class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ll_map = [[1 for i in xrange(n)] for j in xrange(m) ]
        for y in xrange(1,m):
            for x in xrange(1,n):
                ll_map[y][x] = ll_map[y][x-1] + ll_map[y-1][x]
        return ll_map[-1][-1]
