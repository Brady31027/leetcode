class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: return True
        size = len(flowerbed)
        if size == 1:
            if n == 1: return flowerbed[0] == 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n, flowerbed[0] = n - 1, 1
            
        for plot in xrange(1, size - 1, 1):
            if flowerbed[plot] == 0 and flowerbed[plot - 1] == 0 and flowerbed[plot + 1] == 0:
                n, flowerbed[plot] = n - 1, 1
                if n == 0:
                    return True
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n, flowerbed[-1] = n - 1, 1
        
        return n <= 0
        
