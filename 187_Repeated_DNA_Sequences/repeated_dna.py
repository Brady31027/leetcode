class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        ans, memo = set(), set()
        for i in xrange( size - 10 + 1):
            pattern = s[i:i + 10]
            if pattern in memo:
                ans.add(pattern)
            else:
                memo.add(pattern)
        return list(ans)
