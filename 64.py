class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_sum = 9999
        dim_y, dim_x = len(grid), len(grid[0])
        l_sum, l_to_be_traversed = [], [[0,0,grid[0][0]]]
        while l_to_be_traversed:
            node = l_to_be_traversed.pop(0)
            cur_x, cur_y, cur_sum = node[1], node[0], node[2]
            if cur_x == dim_x - 1 and cur_y == dim_y - 1:
                min_sum = min(cur_sum, min_sum)
                continue
            if (cur_x < dim_x - 1) and (cur_y < dim_y - 1):
                l_to_be_traversed.append([cur_y + 1, cur_x, cur_sum + grid[cur_y + 1][cur_x]])
                c = grid[cur_y][cur_x + 1]
                l_to_be_traversed.append([cur_y, cur_x + 1, cur_sum + grid[cur_y][cur_x + 1]])
            elif cur_x < dim_x - 1:
                l_to_be_traversed.append([cur_y, cur_x + 1, cur_sum + grid[cur_y][cur_x + 1]])
            elif cur_y < dim_y - 1:
                l_to_be_traversed.append([cur_y + 1, cur_x, cur_sum + grid[cur_y + 1][cur_x]])
        return min_sum
