class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        memoP, memoT = {}, {}
        tokens = str.split(" ")
        if len(pattern) != len(tokens): return False
        for i in xrange(len(pattern)):
            if not pattern[i] in memoP and not tokens[i] in memoT:
                memoP[ pattern[i] ] = tokens[i]
                memoT[ tokens[i] ] = pattern[i]
            elif (pattern[i] in memoP) != (tokens[i] in memoT):
                return False
            else:
                if memoP[ pattern[i] ] != tokens[i]: return False
                if memoT[ tokens[i] ] != pattern[i]: return False
        return True        
