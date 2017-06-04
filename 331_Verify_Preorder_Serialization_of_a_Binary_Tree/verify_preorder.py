class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        degreeDiff = 1 # out-degree - in-degree
        for node in preorder.split(','):
            degreeDiff -= 1
            if degreeDiff < 0: return False
            if node  != '#':
                degreeDiff += 2
        return degreeDiff == 0
            
        
