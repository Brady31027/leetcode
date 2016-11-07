class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        elif n == 1: return 1
        elif n == 2: return 2
        ans = 0
        for i in xrange(n):
            ans += self.numTrees(i) * self.numTrees(n-i-1)
        return ans
