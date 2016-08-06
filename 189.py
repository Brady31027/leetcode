class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if k == 0 or size == 0:
            return
        tmp = list(nums)
        for i in range(size):
            nums[ (i+k) % size] = tmp[i] 
        
