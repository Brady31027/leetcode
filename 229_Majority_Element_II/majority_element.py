class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        elif len(nums) == 1: return [nums[0]]
        else:
            target_ref = len(nums)//3
            set_nums = set(nums)
            ans = []
            for n in set_nums:
                if nums.count(n) > target_ref:
                    ans.append(n)
            return ans
