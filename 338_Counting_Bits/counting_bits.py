class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def count(num):
            numberOfOne = 0
            while num > 0:
                num = num & (num - 1)
                numberOfOne += 1
            return numberOfOne
            
        returnList = [0]
        for i in range(1, num + 1): # inclusive
            returnList.append( count(i) )
        return returnList
        
