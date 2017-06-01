class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rowLen, colLen, val = len(matrix), len(matrix[0]), matrix[0][0]
        visitedMap = [[False for _ in xrange(colLen)] for _ in xrange(rowLen)]
        heap = [[matrix[0][0], 0, 0]]
        
        for _ in xrange(k):
            val, y, x = heapq.heappop(heap)
            if y + 1 < rowLen and visitedMap[y + 1][x] == False:
                heapq.heappush(heap, [matrix[y + 1][x], y + 1, x])
                visitedMap[y + 1][x] = True
            if x + 1 < colLen and visitedMap[y][x + 1] == False:
                heapq.heappush(heap, [matrix[y][x + 1], y, x + 1])
                visitedMap[y][x + 1] = True
        
        return val
