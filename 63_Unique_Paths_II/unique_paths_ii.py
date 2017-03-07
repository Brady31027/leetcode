class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # corner cases
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1: return 0
        
        size_y, size_x = len(obstacleGrid), len(obstacleGrid[0])
        state = [[1 for x in range(size_x)] for y in range(size_y)]
        
        # overwrite x & y init value if needed
        for x in range(1, size_x):
            if obstacleGrid[0][x] == 1:
                i = x
                while i < size_x: 
                    state[0][i] = 0
                    i += 1
                break
            
        for y in range(1, size_y):
            if obstacleGrid[y][0] == 1:
                i = y
                while i < size_y:
                    state[i][0] = 0
                    i += 1
                break
        # dp the other grids
        for y in range(1, size_y):
            for x in range(1, size_x):
                if obstacleGrid[y][x] == 1:
                    state[y][x] = 0
                else:
                    state[y][x] = state[y-1][x] + state[y][x-1]
        return state[-1][-1]
       
        
