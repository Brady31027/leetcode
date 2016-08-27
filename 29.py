class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN_INT, MAX_INT = -(2**31), 2**31 -1
        minus, result = False, 0
        
        if divisor == 0: return -1
        if dividend == 0: return 0
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0): minus = True
        if divisor < 0: divisor = -divisor
        if dividend < 0: dividend = -dividend
        for i in range(32):
            result = result << 1
            if (dividend >> (31-i) ) >= divisor:
                dividend -= (divisor << (31 - i))
                result += 1
        if minus: 
            result = -result
            return result if result > MIN_INT else MIN_INT
        else: return result if result < MAX_INT else MAX_INT
