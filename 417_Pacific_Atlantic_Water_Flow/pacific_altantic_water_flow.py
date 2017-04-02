class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        size_y, size_x = len(matrix), len(matrix[0])
        visited_coord = [[0 for _ in range(size_x) ] for _ in range(size_y)]
        PAC, ALT = 0, 1
        coord_pac, coord_alt = set(), set()
        
        def dfs(y, x, prev_y, prev_x, ocean):
            if y >= size_y or y < 0 or x >= size_x or x < 0 or visited_coord[y][x] == 1: return
            if ocean == PAC:
                if y == 0 or x == 0 or matrix[y][x] >= matrix[prev_y][prev_x]: coord_pac.add((y, x))
                else: return
            else:
                if y == size_y - 1 or x == size_x - 1 or matrix[y][x] >= matrix[prev_y][prev_x]: coord_alt.add((y, x))
                else: return
            visited_coord[y][x] = 1
            dfs(y-1, x, y, x, ocean)
            dfs(y+1, x, y, x, ocean)
            dfs(y, x-1, y, x, ocean)
            dfs(y, x+1, y, x, ocean)
            return
            
        # subject to Pacific
        for i in range(size_y):
            for j in range(size_x):
                if i != 0 or j != 0: continue
                dfs(i, j, i, j, PAC)
        
        # subject to Atlantic
        visited_coord = [[0 for _ in range(size_x) ] for _ in range(size_y)]
        for i in range(size_y):
            for j in range(size_x):
                if i != (size_y - 1) or j != (size_x - 1): continue
                dfs(i, j, i, j, ALT)
        
        return list(coord_pac & coord_alt)
