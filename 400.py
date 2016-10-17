class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l_long_str = ''
        for i in xrange(n+1):
            l_long_str += str(i)
        return int(l_long_str[i])
