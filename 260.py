class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l_ans, cnt = [], 0
        for i in range(0, len(nums),1):
            if i > 0 and nums[i] == nums[i-1]: continue
            if i+1 == len(nums): 
                l_ans.append(nums[i])
                break
            if nums[i] != nums[i+1]: l_ans.append(nums[i])
        return l_ans  
