class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        memo = collections.defaultdict(int)
        for i in xrange( size - 10 + 1):
            pattern = s[i:i + 10]
            if memo.get(pattern):
                memo[pattern] += 1
            else:
                memo[pattern] = 1
        return filter( lambda key: memo[key] > 1, [key for key in memo])
        
