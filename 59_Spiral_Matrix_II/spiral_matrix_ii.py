class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        spiral = [[ 0 for j in xrange(n)] for i in xrange(n)]
        left, top, right, bottom = 0, 0, n - 1, n - 1
        value = 1
        while left <= right or top <= bottom:
            for x in xrange(left, right + 1):
                if top <= bottom:
                    spiral[top][x] = value
                    value += 1
            for y in xrange(top + 1, bottom + 1):
                if left <= right:
                    spiral[y][right] = value
                    value += 1
            for x in xrange(right - 1, left - 1, -1):
                if top < bottom:
                    spiral[bottom][x] = value
                    value += 1
            for y in xrange(bottom - 1, top, -1):
                if left < right:
                    spiral[y][left] = value
                    value += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return spiral
