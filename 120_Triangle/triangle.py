class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        if height < 2: 
            return 0 if height == 0 else triangle[0][0]
        
        for y in range(1, height):
            width = len(triangle[y])
            for x in range(width):
                if x == 0:
                    triangle[y][x] += triangle[y-1][x] 
                elif x == width - 1:
                    triangle[y][x] += triangle[y-1][x-1]
                else:
                    triangle[y][x] += min(triangle[y-1][x], triangle[y-1][x-1])
        return min(triangle[-1])
