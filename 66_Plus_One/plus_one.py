class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        total = digits[-1] + 1
        carry, digits[-1] = (total / 10), (total % 10)
        for i in xrange(len(digits)-2,-1,-1):
            total = carry + digits[i]
            carry = total / 10
            digits[i] = total % 10
        if carry > 0: digits = [1] + digits
        return digits
