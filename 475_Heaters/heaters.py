class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        result, numHeaters = 0, len(heaters)
        
        heaters.sort()    
        for house in houses:
            # binary search
            index, tail = 0, numHeaters
            while index < tail:
                mid = index + (tail - index) / 2
                if heaters[mid] < house:
                    index = mid + 1
                else:
                    tail = mid
            
            leftDist = house - heaters[index - 1] if index > 0 else sys.maxint
            rightDist = heaters[index] - house if index < numHeaters else sys.maxint
            result = max(result, min(leftDist, rightDist))
        return result
