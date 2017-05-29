class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        if num < 0: num += 0x100000000
        ans, hexTbl = "", "0123456789abcdef"
        while num:
            ans = hexTbl[num % 16] + ans
            num //= 16
        return ans
