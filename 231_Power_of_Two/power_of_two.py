class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n != 0 and n & (n - 1) == 0 else False
