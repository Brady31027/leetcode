class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        l_ans = []
        for i in xrange(1024):
            if bin(i).count('1') == num:
                h, m = i >> 6, i & 0x3F
                if h < 12 and m < 60:
                    l_ans.append("%d:%02d"%(h,m))
        return l_ans
