class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg, result = False, 0
        if x < 0:
            x = -x
            neg = True
        while x > 0:
            result = result * 10 + x % 10
            x = int(x/10)
            if result > (2**31) - 1 or result < -(2 ** 31): return 0
        return result if neg == False else -result
