class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        s, start, end, ans = list(s) + [" "], 0, 0, ""
        for i in xrange(len(s)):
            if s[i] != ' ':
                end = i
            else:
                strList = reversed(s[start: end + 1])
                ans += "".join(strList) + " "
                start = i + 1
        return ans[:-1]
        
