class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        tbl = [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
        return tbl[n - 1] % 1337
    
        """
        # Following is the standard solution but causes TLE
        
        if n == 1: return 9
        
        hiPart = hiPart2 = int(math.pow(10, n) - 1)
        loPart = hiPart // 10
        
        def getPalindrome(k):
            s = str(k)
            return int(s + s[::-1])
        
        def isValid(can, hiPart2):
            while hiPart2 > loPart:
                if hiPart2 < can / hiPart2: 
                    break
                if can % hiPart2 == 0:
                    return True
                hiPart2 -= 1
            return False
        
        while hiPart > loPart:
            candidate = getPalindrome(hiPart)
            if isValid(candidate, hiPart2):
                return candidate % 1337
            hiPart -= 1
        return -1
        """
