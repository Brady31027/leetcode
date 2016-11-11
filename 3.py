class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_c, max_len = [], 0
        for c in s:
            while c in l_c:
                l_c.pop(0)
            l_c.append(c)
            if len(l_c) > max_len: max_len = len(l_c)
        return max_len
