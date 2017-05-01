class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in t:
            if c not in s: return c
            else:
                if s.count(c) != t.count(c): return c
