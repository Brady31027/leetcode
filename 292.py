class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n % 4 != 0)
        """
        Don't know why the following bitwise method is slower than the above % method
        """
        # msk_3 = 0x3
        # return True if (n & msk_3 != 0 ) else False
