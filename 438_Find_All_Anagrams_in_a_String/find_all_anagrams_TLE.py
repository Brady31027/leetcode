class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        # sliding window
        for i in xrange(len(s) - len(p) + 1):
            if sorted( s[i: i + len(p)] ) == sorted( p ):
                ans.append(i)
        return ans
