class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while nums[left] + nums[right] != target:
            if nums[left] + nums[right] > target: right -= 1
            else: left += 1
        return [left+1, right+1]
