class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # identify zeros' coordinates
        l_zero = []
        dim_x, dim_y = len(matrix[0]), len(matrix)
    
        for y in xrange(dim_y):
            for x in xrange(dim_x):
                if matrix[y][x] == 0:
                    l_zero.append((x,y))
        
        # change matrix value to zero if needed
        l_row, l_col = [], []
        for t in l_zero:
            if t[0] not in l_col: l_col.append(t[0])
            if t[1] not in l_row: l_row.append(t[1])
        for x in l_col:
            for y in xrange(dim_y):
                matrix[y][x] = 0
        for y in l_row:
            for x in xrange(dim_x):
                matrix[y][x] = 0
        
