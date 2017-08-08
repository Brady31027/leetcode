class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums)
        lenNums = len(setNums)
        actualSum = sum(nums)
        idealSum = sum(setNums)
        geoSum = ( (lenNums + 2) * (lenNums + 1) ) // 2
        return [actualSum - idealSum, geoSum - idealSum]
