class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k: return s[::-1]
        rev, ans = True, ""
        for i in xrange(0, len(s), k):
            ss = s[i: i+k]
            ss = ss[::-1] if rev else ss
            ans += ss
            rev = not rev
        return ans
        
