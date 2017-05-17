class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = collections.Counter(s)
        for i in xrange(len(s)):
            if hashTable[ s[i] ] == 1:
                return i
        return -1
