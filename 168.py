"""
https://discuss.leetcode.com/topic/6245/python-solution-with-explanation
https://discuss.leetcode.com/topic/47463/simple-python-solution
"""

class Solution(object):
    
    # move table to global is more efficient
    capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            # use divmod is faster
            n, r = divmod(n-1, 26)
            result = self.capitals[r] + result 
        return result
