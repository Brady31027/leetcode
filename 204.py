import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime_cnt = 0
        for i in range( 3, n, 2 ):
            is_prime = True
            for j in range(3, int(math.sqrt(i))+1, 2):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime == True:
                prime_cnt += 1
        return prime_cnt + 1
