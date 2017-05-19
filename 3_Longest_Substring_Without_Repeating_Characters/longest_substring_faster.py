class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, maxLength, tbl = 0, 0, collections.defaultdict(int)
        for i in xrange(len(s)):
            if s[i] in tbl and start <= tbl[s[i]]:
                start = tbl[ s[i] ] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            tbl[ s[i] ] = i
        return maxLength
