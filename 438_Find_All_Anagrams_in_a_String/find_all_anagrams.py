class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counterS, counterP = collections.Counter(), collections.Counter(p)
        start, end, ans = 0, 0, []
        patternSize = len(p)
        for i in xrange(len(s)):
            counterS[ s[i] ] += 1
            end += 1
            if end - start > patternSize:
                counterS[ s[start] ] -= 1
                if counterS[ s[start] ] == 0:
                    del counterS[ s[start] ]
                start += 1
            if counterS == counterP:
                ans.append(start)
        return ans        
