class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dim_y, dim_x = len(grid), len(grid[0])
        dp = [[0 for i in xrange(dim_x)] for j in xrange(dim_y)]
        dp[0][0] = grid[0][0]
        # for x axis
        for i in xrange(1, dim_x): dp[0][i] = dp[0][i-1] + grid[0][i]  
        # for y axis
        for j in xrange(1, dim_y): dp[j][0] = dp[j-1][0] + grid[j][0]
        # start dp
        for y in xrange(1, dim_y):
            for x in xrange(1, dim_x):
                dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y][x]
        return dp[dim_y - 1][dim_x - 1]
