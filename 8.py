import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        str = re.sub(r'^\s+','',str)
        refined_str = ""
        for i in xrange(len(str)):
            if (i == 0 and (str[0] == '-' or str[0] == '+')) or (str[i] <= '9' and str[i] >= '0'):
                refined_str += str[i]
            else:
                break
        if (len(refined_str) == 1 and (refined_str[0] == '-' or refined_str[0] == '+')) or len(refined_str) < 1:
            return 0
        result = int(refined_str)
        if result >= 0:
            return result if result <= MAX_INT else MAX_INT
        else:
            return result if result >= MIN_INT else MIN_INT
