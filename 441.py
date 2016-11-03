class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        level, consume = 0, 1
        while n >= consume:
            n -= consume
            consume += 1
            level += 1
        return level
