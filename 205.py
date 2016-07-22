class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_pattern = {}
        pattern_len = len(s)
        for i in xrange(pattern_len):
            if t[i] in dict_pattern.values():
                if s[i] not in dict_pattern.keys():
                    return False
            if s[i] in dict_pattern.keys():
                if t[i] != dict_pattern.get(s[i]):
                    return False
            else:
                dict_pattern[s[i]] = t[i]
        return True
