class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # from wiki, apply n ^ (n>>1) to convery binary to reflected binary
        return [ i ^ (i >> 1) for i in range(2**n)]
        
