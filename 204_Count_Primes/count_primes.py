class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratorsthenes
        if n <= 2: return 0
        primeBook = [1] * n # total (n) elements from 0 to (n-1)
        primeBook[0] = primeBook[1] = 0
        for base in xrange(2, n):
            if primeBook[base]:
                for derive in xrange(base * 2, n, base):
                    primeBook[derive] = 0
        return sum(primeBook)
