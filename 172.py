class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros = 0
        for i in range(1, n+1, 1):
            #print i
            if i % 10 == 0:
                zeros += 1
            elif i % 5 == 0:
                zeros += 1
        return zeros
