class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if j > i: matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(len(matrix)): matrix[i].reverse()
        
        
