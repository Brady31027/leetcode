class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # corner cases
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0
        x_dim, y_dim = len(obstacleGrid[0]), len(obstacleGrid)
        ll_map = [[1 for x in xrange(x_dim)] for y in xrange(y_dim)]
        # init obstacle in map
        x_block, y_block = x_dim + 1, y_dim + 1
        for y in xrange(y_dim):
            if obstacleGrid[y][0] == 1:
                y_block = y
                break
        for x in xrange(x_dim):
            if obstacleGrid[0][x] == 1:
                x_block = x
                break
        if y_block < y_dim:
            for y in xrange(y_block, y_dim):
                ll_map[y][0] = 0
        if x_block < x_dim:
            for x in xrange(x_block, x_dim):
                ll_map[0][x] = 0
        # start dp traversal
        for y in xrange(1, y_dim):
            for x in xrange(1, x_dim):
                if obstacleGrid[y][x] == 1:
                    ll_map[y][x] = 0
                    continue
                ll_map[y][x] = ll_map[y-1][x] + ll_map[y][x-1]
        return ll_map[-1][-1]
                
        
