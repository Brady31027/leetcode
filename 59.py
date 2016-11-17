class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        elif n == 1: return [[1]]
        ll_ans = [[0 for _x in xrange(n)] for _y in xrange(n)]
        ll_map = ll_ans
        ll_ans[0][0], ll_map[0][0] = 1, 1
        total_nodes = n * n
        traversed_nodes = 0
        x, y, val = 0, 0, 2
        while traversed_nodes < total_nodes:
            while x + 1 < n and ll_map[y][x+1] == 0:
                x += 1
                ll_ans[y][x] = val
                ll_map[y][x] = 1
                val += 1
                traversed_nodes += 1
            while y + 1 < n and ll_map[y+1][x] == 0:
                y += 1
                ll_ans[y][x] = val 
                ll_map[y][x] = 1
                val += 1
                traversed_nodes += 1
            while x - 1 >= 0 and ll_map[y][x-1] == 0:
                x -= 1
                ll_ans[y][x] = val 
                ll_map[y][x] = 1
                val += 1
                traversed_nodes += 1
            while y - 1 >= 0 and ll_map[y-1][x] == 0:
                y -= 1
                ll_ans[y][x] = val 
                ll_map[y][x] = 1
                val += 1
                traversed_nodes += 1
        return ll_ans
        
