class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nonzeroProduct, product, tbl = 1, 1, collections.Counter(nums)
        if tbl[0] > 1: return [0] * len(nums)
        for k, v in tbl.items():
            if k != 0: nonzeroProduct *= (k ** v)
        
        if tbl[0] > 0: product = 0
        else: product = nonzeroProduct
        
        for i in xrange(len(nums)):
            if nums[i] == 0: nums[i] = nonzeroProduct
            else: nums[i] = product // nums[i]
        return nums
            
        
        
