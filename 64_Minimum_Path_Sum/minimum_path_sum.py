class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size_y, size_x = len(grid), len(grid[0])
        state= [[0 for i in range(size_x)] for j in range(size_y)]
        state[0][0] = grid[0][0]
        for x in range(1, size_x):
            state[0][x] = grid[0][x] + state[0][x-1]
        for y in range(1, size_y):
            state[y][0] = grid[y][0] + state[y-1][0]
        for y in range(1, size_y):
            for x in range(1, size_x):
                state[y][x] = grid[y][x] + min(state[y-1][x], state[y][x-1])
        return state[-1][-1]
