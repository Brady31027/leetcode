class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s) == 0 else 0 if len(s.split()) == 0  else len(s.split()[-1])
        
