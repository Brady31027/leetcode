class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True
        m = n
        while n > 5:
            for i in [2,3,5]:
                if n % i == 0:
                    n /= i
            if m == n:
                return False
            else:
               m = n
        return True
