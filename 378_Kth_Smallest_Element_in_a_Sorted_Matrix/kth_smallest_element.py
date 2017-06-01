class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rowLen, colLen = len(matrix), len(matrix[0])
        visitedMap = set()
        
        def expend(y, x):
            if y + 1 < rowLen and (y + 1, x) not in visitedMap:
                heapq.heappush(heap, [matrix[y + 1][x], y + 1, x])
                visitedMap.add((y + 1, x))
            if x + 1 < colLen and (y, x + 1) not in visitedMap:
                heapq.heappush(heap, [matrix[y][x + 1], y, x + 1])
                visitedMap.add((y, x + 1))
        heap = [[matrix[0][0], 0, 0]]
        heapq.heapify(heap)
        
        val = matrix[0][0]
        for _ in xrange(k):
            val, y, x = heapq.heappop(heap)
            expend(y, x)
            
        return val
