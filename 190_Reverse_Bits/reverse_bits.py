class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binStr = "%032d" % int(str( bin(n) )[2:])
        reverseBinStr = binStr[::-1]
        return int(reverseBinStr, 2)
