class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # e.g [1, 1] to [1, 2, 1]
        # extend [1, 1] to [0, 1, 1] and [1, 1, 0]
        # sum up [0, 1, 1] and [1, 1, 0] to form [1, 2, 1]
        if numRows == 0: return []
        ans = [[1]]
        for i in xrange(1, numRows):
            ans += [map(lambda x, y: x + y, [0] + ans[-1], ans[-1] + [0])]
        return ans
        
