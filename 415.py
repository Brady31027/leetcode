class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        int1, int2 = 0, 0
        for i,c in enumerate(num1):
            int1 += (ord(c) - ord('0')) * pow(10, (len1 - i - 1))
        for i,c in enumerate(num2):
            int2 += (ord(c) - ord('0')) * pow(10, (len2 - i - 1)) 
        return str(int1+int2)
