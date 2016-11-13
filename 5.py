class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_substring = ""
        
        def getPalindrome(s, start, end):
            size = len(s)
            while start >= 0 and end < size and s[start] == s[end]:
                start, end = start - 1, end + 1
            return s[start+1:end]
        
        for i in xrange(len(s)):
            max_substring1 = getPalindrome(s, i, i)
            max_substring2 = getPalindrome(s, i, i+1)
            max_substring1 = max_substring1 if len(max_substring1) > len(max_substring2) else max_substring2
            max_substring = max_substring1 if len(max_substring1) > len(max_substring) else max_substring
        return max_substring
                
