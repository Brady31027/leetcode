class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        tbl = set()
        for i in xrange(int(math.sqrt(c))+1):
            n = i * i
            tbl.add(n)
            if c - n in tbl:
                return True
        return False
