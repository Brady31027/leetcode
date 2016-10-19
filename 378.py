class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l_flat_matrix = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                l_flat_matrix.append(matrix[y][x])
        l_flat_matrix.sort()
        return l_flat_matrix[k - 1]
        
