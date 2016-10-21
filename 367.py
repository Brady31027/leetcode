class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        for i in xrange(num):
            if i * i > num: return False
            elif i * i == num: return True
        return False
