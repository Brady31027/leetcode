class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        satisfied, child_idx = 0, 0
        g.sort()
        s.sort()
        for cookie_idx in range(len(s)):
            if child_idx == len(g): return satisfied
            if s[cookie_idx] >= g[child_idx]:
                satisfied += 1
                child_idx += 1
        return satisfied
