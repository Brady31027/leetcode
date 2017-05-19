class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftOne = 0
        for char, appearingCnt in collections.Counter(s).iteritems():
            leftOne += int(appearingCnt % 2 == 1)
        return len(s) - leftOne + int(leftOne > 0)    
