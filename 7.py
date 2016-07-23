class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        neg = True if x < 0 else False
        str_input = str(x)
        if neg == True:
            str_input = '-'+str_input[:0:-1]
            return 0 if int(str_input) < MIN_INT else int(str_input)
        else:
            str_input = str_input[::-1]
            return 0 if int(str_input) > MAX_INT else int(str_input)
