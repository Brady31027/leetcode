class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0,len(nums),2):
            if i+1 >= len(nums): return nums[i]
            elif nums[i] != nums[i+1]: return nums[i]
