class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def flood(y, x):
            if y < 0 or y >= size_y or x < 0 or x >= size_x: return
            if grid[y][x] == '1' and visited_map[y][x] == 0:
                visited_map[y][x] = 1
                flood(y-1, x)
                flood(y+1, x)
                flood(y, x-1)
                flood(y, x+1)
        
        if not grid: return 0
        size_x, size_y = len(grid[0]), len(grid)
        visited_map = [ [0 for _ in range(size_x) ] for _ in range(size_y)]
        island = 0
        for y in range(0, size_y):
            for x in range(0, size_x):
                if grid[y][x] == '1' and visited_map[y][x] == 0:
                    island += 1
                    flood(y, x)
        return island
                
