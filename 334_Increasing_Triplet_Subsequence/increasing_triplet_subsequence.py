class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        firstMin = secondMin = float("inf")
        for n in nums:
            if n <= firstMin:
                firstMin = n
            elif n <= secondMin:
                secondMin = n
            else:
                return True
        return False
            
