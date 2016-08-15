#https://discuss.leetcode.com/topic/8692/o-n-time-o-1-space-fastest-solution

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0: major, count = nums[i], 1
            elif nums[i] == major: count += 1
            else: count -= 1
        return major
