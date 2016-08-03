import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        target = math.floor(len(nums) / 2)
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i] += 1
                if dict_nums[i] > target:
                    return i
            else:
                dict_nums[i] = 1
