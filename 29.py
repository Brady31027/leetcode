class Solution(object):
    MAX_INT = (2 ** 31) - 1
    MIN_INT = -(2 ** 31)
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return -1
        elif dividend == 0: return 0
        elif divisor == 1: 
            if dividend > 0: return dividend if dividend < self.MAX_INT else self.MAX_INT
            else: return dividend if dividend > self.MIN_INT else self.MIN_INT
        elif divisor == -1:
            if dividend > 0: return -dividend if -dividend > self.MIN_INT else self.MIN_INT
            else: return -dividend if -dividend < self.MAX_INT else self.MAX_INT
        
        neg = False
        
        if divisor > self.MAX_INT: divisor = self.MAX_INT
        elif divisor < self.MIN_INT: divisor = self.MIN_INT
        
        if dividend > self.MAX_INT: dividend = self.MAX_INT
        elif dividend < self.MIN_INT: dividend = self.MIN_INT
        
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            neg = True
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            neg = True
        
        if dividend < divisor: return 0
        
        ans = 0
        while dividend >= divisor:
            dividend -= divisor
            ans += 1
            if ans > self.MAX_INT: return self.MAX_INT
        
        return ans if neg == False else -ans
            
            
