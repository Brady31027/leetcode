class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charHashS, charHashT = {}, {} # s: t
        for i in xrange(len(s)):
            if s[i] not in charHashS and t[i] not in charHashT:
                charHashS[ s[i] ] = t[i]
                charHashT[ t[i] ] = s[i]
            elif s[i] in charHashS and t[i] not in charHashT:
                return False
            elif s[i] not in charHashS and t[i] in charHashT:
                return False
            elif s[i] in charHashS and t[i] in charHashT:
                if charHashS[ s[i] ] != t[i]: return False
                if charHashT[ t[i] ] != s[i]: return False
        return True
                
        
