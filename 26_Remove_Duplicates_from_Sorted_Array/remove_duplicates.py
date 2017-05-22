class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n, validCursor = nums[0], 0
        for i in xrange(1, len(nums)):
            if nums[i] == n:
                continue
            validCursor += 1
            n = nums[validCursor] = nums[i]
        return validCursor + 1    
