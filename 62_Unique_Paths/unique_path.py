class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        state = [[1 for i in range(n)] for j in xrange(m) ]
        for y in range(1, m):
            for x in range(1, n):
                state[y][x] = state[y-1][x] + state[y][x-1]
        return state[-1][-1]
