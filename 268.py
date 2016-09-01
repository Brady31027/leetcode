class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search could be faster
        nums.sort()
        for i in range(len(nums)):
            if nums[i] - i != 0: return i
        return len(nums)
