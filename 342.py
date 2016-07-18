class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        POWER_OF_FOUR_MSK = 0x55555555
        if (num > 0) and (num & (num-1) == 0) and (num & POWER_OF_FOUR_MSK !=0):
            return True
        else:
            return False
