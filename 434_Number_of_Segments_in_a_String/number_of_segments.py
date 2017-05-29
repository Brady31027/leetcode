class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        return len(s.strip().split())
