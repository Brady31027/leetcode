class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        abs_num = abs(num)
        neg_num = True if num < 0 else False
        seven_base = ''
        while abs_num:
            seven_base += str(abs_num % 7)
            abs_num //= 7
        return '-'+seven_base[::-1] if neg_num else seven_base[::-1]
        
        
