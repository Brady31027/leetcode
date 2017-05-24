class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size, anchor = len(nums), 0
        if size < 2: return
    
        for i in xrange(size - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                anchor = i - 1 # 0
                break
        if anchor + 1 > 0:
            for i in xrange(size - 1, -1, -1):
                if nums[i] > nums[anchor]:
                    nums[i], nums[anchor] = nums[anchor], nums[i]
                    break
        nums[anchor + 1:] = reversed(nums[anchor + 1:])
            
                
                
