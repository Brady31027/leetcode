class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product,zero_cnt = 1, 0
        for n in nums:
            if n == 0:
                zero_cnt +=1
                if zero_cnt > 1: break
                continue
            product *= n
            
        for i in range(len(nums)):
            if zero_cnt > 1: return [0]*len(nums)
            else:
                if nums[i] == 0: nums[i] = product
                elif zero_cnt > 0: nums[i] = 0
                else: nums[i] = product // nums[i]
        return nums
