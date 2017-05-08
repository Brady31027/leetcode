class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos += 1
