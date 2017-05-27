class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        setX, setY = set(), set()
        height, width = len(matrix), len(matrix[0])
        for y in xrange(height):
            for x in xrange(width):
                if matrix[y][x] == 0:
                    setX.add(x)
                    setY.add(y)
        for x in setX:
            for y in xrange(height):
                matrix[y][x] = 0
        for y in setY:
            for x in xrange(width):
                matrix[y][x] = 0
        
