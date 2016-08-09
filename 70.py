class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(0) = stop         -> 1
        # f(1) = 1            -> 1
        # f(2) = 1+1   or 2   -> 2
        # f(3) = 1+1+1 or 2+1 or 1+2 = f(2) + 1 or f(1) + 2 = f(1) + f(2)
        # f(n) = f(n-1) + f(n-2)a
        
        return 1 if n < 2 else self.climbStairs(n-1) + self.climbStairs(n-2)
