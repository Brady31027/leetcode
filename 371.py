class Solution(object):
    def getSum(self, a, b):
        MAX_8b = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        # a for result, b for carry
        while b != 0:
            a, b = (a ^ b) & MAX_8b, ( (a & b) << 1) & MAX_8b
        if a <= MAX_INT:
            return a
        else:
            return ~(a & MAX_INT) ^ MAX_INT
