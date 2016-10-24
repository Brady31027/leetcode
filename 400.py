class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l_long_str = ''
        counter = 0
        for i in xrange(1, n+1):
            l_long_str += str(i)
            counter += int(math.log10(i)) + 1
            if counter >= n: break
        return int(l_long_str[n-1])
