class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 6 : 
            if num <= 0: return False
            return True # all of 1, 2, 3, 4, 5 are not ugly
        for div in [2, 3, 5]:
            while num % div == 0:
                num /= div
        return num == 1
