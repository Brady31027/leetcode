class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        size = len(height)
        visited = [0] * size
        heap = [(height[0], 0), (height[ size - 1 ], size - 1) ]
        heapq.heapify(heap)
        water = 0
        
        while heap:
            h, x = heapq.heappop(heap)
            for newX in [x - 1, x + 1]:
                if 0 < newX < size - 1 and visited[newX] == 0:
                    water += max(0, h - height[newX])            
                    heapq.heappush(heap, ( max(h, height[newX]), newX))
                    visited[newX] = 1
        return water
            
        
