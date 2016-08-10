class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [Sieve of Eratorsthenes]
        # => if number a is mutiple of number b, then a is not a prime
        # useful hints: xrange uses less memory than range
        if n <= 2: return 0
        l_is_prime = [1] * n
        for i in xrange(2, n):
            if l_is_prime[i]:
                for j in xrange( i * 2, n, i):
                    l_is_prime[j] = 0
        return l_is_prime.count(1)-2 # 0 and 1 are not prime
