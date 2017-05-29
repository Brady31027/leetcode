class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        for i in xrange(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]
        
