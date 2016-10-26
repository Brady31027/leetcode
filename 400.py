class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        for i in range(1024): # what is the exact value?
            start = 9 * 10 ** i
            if start * (i+1) >= n: break
            n -= start * (i+1)
            digit_len += 1
        hold_num = 10**i + (n-1) // digit_len
        hold_digit = (n-1) % digit_len
        return int(str(hold_num)[hold_digit])

