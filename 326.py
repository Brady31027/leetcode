class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
        #return True if n > 0 and (math.log10(n)/math.log10(3)).is_integer() else False
        #return True if n > 0 and if n > 0 and (3**round(math.log(n, 3)) == n) else False
        
