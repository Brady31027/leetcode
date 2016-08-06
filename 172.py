class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n/5 + n/25 + n/125 + ... + n/(5**k)
        cnt, div = 0, 5
        while div <= n:
            cnt += (n/div)
            div *= 5
        return cnt
        
