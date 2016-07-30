class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        cnt = len(s)
        for c in s:
            ret += ( ord(c) - ord('A') + 1 ) * (26 ** (cnt - 1) )
            cnt -= 1
        return ret
