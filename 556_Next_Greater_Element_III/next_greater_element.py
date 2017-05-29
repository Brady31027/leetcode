class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        strN, anchor = list(str(n)), -1
        for i in xrange(len(strN) - 1, -1, -1):
            if i - 1 >= 0 and strN[i] > strN[i - 1]:
                anchor = i - 1
                break
        if anchor == -1: return -1
        for i in xrange(len(strN) - 1, anchor, -1):
            if strN[anchor] < strN[i]:
                strN[anchor], strN[i] = strN[i], strN[anchor]
                break
        strN[anchor + 1::] = reversed(strN[anchor + 1::])
        ans = int("".join(strN))
        return ans if ans < 0x80000000 else -1
