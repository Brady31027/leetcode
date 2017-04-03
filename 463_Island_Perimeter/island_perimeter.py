class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size_y, size_x = len(grid), len(grid[0])
        perimeter = 0
        for y in range(size_y):
            for x in range(size_x):
                if grid[y][x] == 1: 
                    perimeter += 4
                    if y > 0 and grid[y-1][x] == 1: perimeter -= 2
                    if x > 0 and grid[y][x-1] == 1: perimeter -= 2
        return perimeter
