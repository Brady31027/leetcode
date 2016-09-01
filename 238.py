class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = [0]*len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j: continue
                else:
                    product *= nums[j]
                if product == 0: break
            nums2[i] = product
        return nums2
