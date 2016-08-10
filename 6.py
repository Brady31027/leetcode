class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) < numRows: return s
        
        ll_zz = [[] for i in range(numRows + 1)]
        y_coord, y_delta = 0, 1 # down
        for c in s:
            ll_zz[y_coord].append(c)
            if y_coord == 0: y_delta = 1
            elif y_coord == numRows - 1: y_delta = -1
            y_coord += y_delta
        return "".join(reduce(operator.add, ll_zz))
