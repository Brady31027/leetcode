class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len, max_substring = 0, ""
        
        def isPalindrome(s):
            return True if s == s[::-1] else False
        
        for i in xrange(0, len(s)):
            for j in xrange(0, i+1):
                if isPalindrome(s[j:i+1]) == True:
                    max_len = max(max_len, i - j + 1)
                    if max_len == (i - j + 1): max_substring = s[j:i+1]
        return max_substring
                
                
