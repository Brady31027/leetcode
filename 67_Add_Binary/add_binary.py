class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin( int(str(a), 2) + int(str(b), 2) ))[2:]
        
