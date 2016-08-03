class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = bin(n)[2::]
        padding_zero = ''
        for i in range( 32 - len(result)):
            padding_zero += '0'
        result = padding_zero + result
        return int(result[::-1], 2)
