class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_len, ll_b = 0, [[0 for _col_ in xrange(len(matrix[0]))] for _row_ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i == 0 or j == 0: ll_b[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1': ll_b[i][j] = min(ll_b[i-1][j],ll_b[i-1][j-1],ll_b[i][j-1]) + 1
                max_len = max(max_len, ll_b[i][j])
        return max_len * max_len
