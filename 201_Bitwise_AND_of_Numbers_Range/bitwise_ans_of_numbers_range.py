class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = m
        for number in range(m+1, n+1):
            ans &= number
        return ans
        
