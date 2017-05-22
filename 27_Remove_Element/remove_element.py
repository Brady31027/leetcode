class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        validCursor = 0
        for i in xrange(len(nums)):
            if nums[i] == val:
                continue
            nums[validCursor] = nums[i]
            validCursor += 1
        return validCursor    
            
