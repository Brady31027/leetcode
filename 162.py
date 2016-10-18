class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = sorted(set(nums))
        for i, v in enumerate(nums):
            if v == set_nums[-1]: return i
