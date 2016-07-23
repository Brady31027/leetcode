class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        reverse_str_x = str_x[::-1]
        return True if str_x == reverse_str_x else False
