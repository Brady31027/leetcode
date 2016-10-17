class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        l_ans = []
        l_hex = "0123456789abcdef"
        if num < 0: num += 0x100000000
        while num:
            l_ans.append( l_hex[num % 16] )
            num //= 16
        return ''.join(l_ans[::-1])
