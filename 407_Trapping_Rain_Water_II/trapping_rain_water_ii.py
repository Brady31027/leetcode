class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap: return 0
        row, col, heap = len(heightMap), len(heightMap[0]), []
        visited = [[0] * col for _ in xrange(row)]
        for y in xrange(row):
            for x in xrange(col):
                if (y == 0 or x == 0 or y == row - 1 or x == col - 1) and (visited[y][x] == 0):
                    heapq.heappush(heap, [ heightMap[y][x], y, x ] )
                    visited[y][x] = 1
        water = 0
        while heap:
            height, y, x = heapq.heappop(heap)
            for expandY, expandX in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 < expandY < row - 1 and 0 < expandX < col - 1 and visited[expandY][expandX] == 0:
                    water += max(0, height - heightMap[expandY][expandX])
                    heapq.heappush(heap, [ max(height, heightMap[expandY][expandX]), expandY, expandX ] )
                    visited[expandY][expandX] = 1
        return water
                    
            
