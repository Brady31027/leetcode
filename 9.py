class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # [version 2]
        while num > 0:
            reverse_num = (reverse_num * 10) + (num % 10)
            num /= 10
        return True if reverse_num == x else False
'''
        # [version 1]
        str_x = str(x)
        reverse_str_x = str_x[::-1]
        return True if str_x == reverse_str_x else False
'''
