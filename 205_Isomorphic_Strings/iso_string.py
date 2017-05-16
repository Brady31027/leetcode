class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charHashS, charHashT = {}, {} # s: t
        for i in xrange(len(s)):
            if not s[i] in charHashS and not t[i] in charHashT:
                charHashS[ s[i] ] = t[i]
                charHashT[ t[i] ] = s[i]
            elif (s[i] in charHashS) != (t[i] in charHashT): # xor
                return False
            else:
                if charHashS[ s[i] ] != t[i]: return False
                if charHashT[ t[i] ] != s[i]: return False
        return True
                
         
        
