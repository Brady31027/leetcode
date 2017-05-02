class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # total 10 LEDs, the max number is 2 ** 10 = 1024
        MAX_NUM = 1024
        represetedTime = []
        for i in xrange(MAX_NUM):
            if bin(i).count('1') == num: # if number of 1 matches
                # hour: higher 4 bits
                #       i >> 6
                # minute: lower 6 bits
                #       i & 0b111111 == i & 64 == i & 0x3F
                h, m = i >> 6, i & 0x3F
                if h < 12 and m < 60:
                    represetedTime.append("%d:%02d"%(h,m))
        return represetedTime
