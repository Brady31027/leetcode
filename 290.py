class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        l_str = str.split()
        if len(pattern) != len(l_str):
            return False
        if len( set(pattern) ) != len( set(l_str) ):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                if l_str[i] != d.get(pattern[i]):
                    return False
            else:
                d[ pattern[i] ] = l_str[i] 
        return True
