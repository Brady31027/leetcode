class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getCntForDigit(m):
            total, factor, tmp_m = 1, 9, m
            while tmp_m > 0:
                total *= factor
                if tmp_m < m: factor -= 1
                tmp_m -= 1
            return total
        
        if n == 0: return 1    
        cnt = 0
        for i in range(n,0,-1):
            if i > 1:
                cnt += getCntForDigit(i)
            else: cnt += 10
        return cnt
