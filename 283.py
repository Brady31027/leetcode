class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_cnt = nums.count(0)
        for i in xrange( zero_cnt):
            nums.remove(0)
            nums.append(0)
