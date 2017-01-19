class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        lazy approach: bin(n).count('1')
        """
        result = 0
        while n:
            n &= (n-1)
            result += 1
        return result
