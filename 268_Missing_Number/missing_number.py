class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search could be faster
        #nums.sort()
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)
