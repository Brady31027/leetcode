class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: return s
        board = [[] for _ in xrange(numRows)]
        y, step = 0, 1
        for c in s:
            if y == 0: step = 1
            elif y == numRows - 1: step = -1
            board[y].append(c)
            y += step
        ans = ""
        for i in xrange(numRows): ans += "".join(board[i])
        return ans
            
