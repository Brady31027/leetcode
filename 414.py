class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_set_nums = list(set(nums))
        if len(l_set_nums) == 1: return l_set_nums[0]
        elif len(l_set_nums) == 2: return max(l_set_nums[0], l_set_nums[1])
        else: return sorted(l_set_nums,reverse=True)[2]
