class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_s = set(s)
        odd_c = []
        for c in set_s:
            if s.count(c) % 2 != 0:
                if c not in odd_c: odd_c.append(c)
                else: odd_c.remove(c)
        return len(s) - max(0, len(odd_c) - 1) 
