class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 and (3**round(math.log(n, 3)) == n):
            return True
        else:
            return False

        
