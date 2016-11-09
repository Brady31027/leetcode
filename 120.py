class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        size = len(triangle)
        if size == 1: return triangle[0][0]
        for y in xrange(1, size):
            for x in xrange(y+1):
                up_enable = (x < y)
                upper_left_enable = (x-1 >= 0)
                if up_enable and upper_left_enable:
                    triangle[y][x] += min(triangle[y-1][x-1], triangle[y-1][x])
                elif up_enable:
                    triangle[y][x] += triangle[y-1][x] #up
                else:
                    triangle[y][x] += triangle[y-1][x-1] #upper_left
        return min(triangle[-1])
