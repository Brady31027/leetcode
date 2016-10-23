class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        perfect_square = 0
        for i in range(1, n+1):
            if int(math.sqrt(i)+0.5) ** 2 == i:
                perfect_square += 1
        return perfect_square
