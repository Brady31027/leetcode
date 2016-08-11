class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        while num > 0:
            reverse_num = (reverse_num * 10) + (num % 10)
            num /= 10
        return reverse_num == x
