class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] > target: break
                elif i == j: continue
                elif nums[i] + nums[j] == target: return [min(i+1,j+1), max(i+1,j+1)]
        return []
