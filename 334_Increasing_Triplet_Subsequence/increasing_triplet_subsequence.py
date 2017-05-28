class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        minimal = firstMin = secondMin = float("inf")
        for n in nums:
            if n <= minimal:
                minimal = n
            elif n <= secondMin:
                firstMin, secondMin = minimal, n
            else:
                return True
        return False
            
