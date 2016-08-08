class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == 0: return b
        elif b == 0: return a
        
        bin_sum = bin(int(a,2) + int(b,2))
        return bin_sum[2: len(bin_sum)]
