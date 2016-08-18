class Solution(object):
    """
    https://discuss.leetcode.com/topic/53627/python-solution-beats-90-list-16-possible-power-of-4-in-all-32-bit-integers/2
    """
    def isPowerOfFour(self, n):
        str_hex = str(hex(n)[2:])
        if str_hex[0] != '1' and str_hex[0] != '4': return False
        for i in xrange(1, len(str_hex)):
            if str_hex[i] != '0': return False
        return True
