class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in xrange(1, rowIndex + 1):
            ans = map(lambda x, y: x + y, [0] + ans, ans + [0])
        return ans
        
