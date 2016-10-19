class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for y in xrange(len(matrix)):
            for x in xrange(len(matrix[0])):
                if matrix[y][x] == target: return True
                elif matrix[y][x] > target: break
        return False
