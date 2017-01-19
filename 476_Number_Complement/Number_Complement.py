class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        upper_bound = 1
        while upper_bound <= num:
            upper_bound *= 2
        return (upper_bound - 1) ^ num
