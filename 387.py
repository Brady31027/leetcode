class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        for x, c in enumerate(s):
            if d[c] == 1:
                return x
        return -1
