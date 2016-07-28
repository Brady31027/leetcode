class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dict_roman = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        for i in range(len(s)):
            if i > 0 and dict_roman[ s[i] ] > dict_roman[ s[i-1] ]:
                result += dict_roman[ s[i] ] - 2 * dict_roman[ s[i-1] ]
            else:
                result += dict_roman[ s[i] ]
        return result    
