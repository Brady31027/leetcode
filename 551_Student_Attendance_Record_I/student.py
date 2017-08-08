class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = re.findall('L{3,}', s)
        if len(result) > 0: return False
        result = re.findall('A', s)
        if len(result) > 1: return False 
        return True
        
        
