class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        l_ans = [matrix[0][0]]
        dim_x, dim_y = len(matrix[0]), len(matrix)
        total_node, x, y, traversed_node = dim_x * dim_y, 0, 0, 1
        ll_map = [[0 for _x in xrange(dim_x)] for _y in xrange(dim_y)]
        ll_map[0][0] = 1
        while traversed_node < total_node:
            while x + 1 < dim_x and ll_map[y][x+1] == 0: # e
                x += 1
                traversed_node += 1
                ll_map[y][x] = 1
                l_ans.append(matrix[y][x])
            while y+1 < dim_y and ll_map[y+1][x] == 0: # s
                y += 1
                traversed_node += 1
                ll_map[y][x] = 1
                l_ans.append(matrix[y][x])
            while x-1 >= 0 and ll_map[y][x-1] == 0: # w
                x -= 1
                traversed_node += 1
                ll_map[y][x] = 1
                l_ans.append(matrix[y][x])
            while y-1 >= 0 and ll_map[y-1][x] == 0: # n
                y -= 1
                traversed_node += 1
                ll_map[y][x] = 1
                l_ans.append(matrix[y][x])
        return l_ans
