class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s, set_t = {}, set()
        for (src, tar) in zip(s, t):
            if src in dict_s:
                if dict_s[src] != tar:
                    return False
            else:
                if tar in set_t:
                    return False
                dict_s[src] = tar
                set_t.add(tar)
            """
            # following method is still failed the performance test
            if dict_s.get(src) == None and dict_t.get(tar) == None:
                dict_s[src] = tar
                dict_t[tar] = src
            elif dict_s.get(src) != tar or dict_t.get(tar) != src:
                return False
            """
        return True
        
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
        """
