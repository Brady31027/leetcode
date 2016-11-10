class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < min_num: return nums[i]
        return min_num
