class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_c, max_len, j = [], 0, 0
        for i in xrange(len(s)):
            while s[i] in l_c[j:]: j += 1
            l_c.append(s[i])
            if i - j + 1 > max_len: max_len = i - j + 1
        return max_len
