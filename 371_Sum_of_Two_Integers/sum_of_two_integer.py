class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # current digit: a ^ b
        # carry digit: a & b
        MAX = 0x7FFFFFFF
        MSK = 0xFFFFFFFF
        
        while b != 0:
            carry = (a & b) & MSK
            a = (a ^ b) & MSK
            b = (carry << 1) & MSK
        return a if a <= MAX else ~(a ^ MSK)
