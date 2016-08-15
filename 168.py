class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = ''
        while n > 0:
            result = capitals[(n-1)%26] + result
            n = (n-1) // 26
        return result
