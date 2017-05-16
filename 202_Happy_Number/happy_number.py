class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numberBook = set()
        while True:
            newN, strN = 0, str(n)
            for char in strN:
                newN += int(char) ** 2
            if newN in numberBook:
                return False
            if newN == 1:
                return True
            n = newN
            numberBook.add(newN)
                
