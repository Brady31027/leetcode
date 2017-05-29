class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        s, start, end, ans = s + " ", 0, 0, ""
        for i in xrange(len(s)):
            if s[i] != ' ':
                end = i
            else:
                strList = list(s[start: end + 1])
                head, tail = 0, len(strList) - 1
                while head < tail:
                    strList[head], strList[tail] = strList[tail], strList[head]
                    head, tail = head + 1, tail - 1
                ans += "".join(strList) + " "
                start = i + 1
        return ans[:-1]
        
