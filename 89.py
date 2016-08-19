class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # from wiki, apply n ^ (n>>1) to convery binary to reflected binary
        l_result = []
        for i in range(2**n):
            l_result.append(i ^ (i >> 1))
        return l_result
        
