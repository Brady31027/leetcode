class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        str = str.lstrip() # remove heading spaces
        negative = False
        if str[0] == '+':
            str = str[1:] # remove leading + 
            if not str or not str[0].isdigit(): return 0 # sign symbol can only appear once
        if str[0] == '-':
            negative = True
            str = str = str[1:] # remove leading - 
            if not str or not str[0].isdigit(): return 0 # sign symbol can only appear once
            
        validStr = ""
        for c in str:
            if c.isdigit(): # atoi doesn't need to consider floating point
                validStr += c
            else: break
        if not validStr: return 0
        validNum = -int(validStr) if negative else int(validStr)
        
        # handle range
        if validNum > 2147483647: validNum = 2147483647
        elif validNum < -2147483648: validNum = -2147483648
        return validNum
