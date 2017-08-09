class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minX, minY = sys.maxint, sys.maxint
        for op in ops:
            minY = min(minY, op[0])
            minX = min(minX, op[1])
        return min(n, minX) * min(m, minY)
