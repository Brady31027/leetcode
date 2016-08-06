import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub("\W+","",s.lower())
        t = s[::-1]
        return True if s == t else False
        
