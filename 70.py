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
        
        # recursive is too slow
        # return 1 if n < 2 else self.climbStairs(n-1) + self.climbStairs(n-2)
        l_fib = [1 for i in range(n+1)]
        for i in range(2,n+1,1):
            l_fib[i] = l_fib[i-1] + l_fib[i-2]
        return l_fib[n]
