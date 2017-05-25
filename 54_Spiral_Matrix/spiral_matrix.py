class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        spiral = []
        while left <= right or top <= bottom:
            for x in xrange(left, right + 1):
                if top <= bottom:
                    spiral.append(matrix[top][x])
            for y in xrange(top + 1, bottom + 1):
                if left <= right:
                    spiral.append(matrix[y][right])
            for x in xrange(right - 1, left - 1, -1):
                if top < bottom:
                    spiral.append(matrix[bottom][x])
            for y in xrange(bottom - 1, top, -1):
                if left < right:
                    spiral.append(matrix[y][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return spiral
        
