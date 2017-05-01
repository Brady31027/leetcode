class Solution(object):
    def isPowerOfFour(self, num):
        if num > 0 and num & (num - 1) == 0:
            binStr = "%032d" % int(str(bin(num))[2:])
            if binStr.find('1') % 2 != 0:
                return True
        return False
