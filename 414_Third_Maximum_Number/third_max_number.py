class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3: return nums[0]
        return nums[2]
