class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, perfect_square = 1, 0
        while i < n + 1:
            if i ** 2 < n + 1:
                perfect_square += 1
            else: break
            i += 1
        return perfect_square
