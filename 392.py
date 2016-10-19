class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set_t = set(t)
        l_s = list(s)
        for ss in s:
            if ss not in set_t: return False
        for tt in t:
            if len(l_s) > 0 and l_s[0] == tt: l_s.pop(0)
        return True if len(l_s) == 0 else False
