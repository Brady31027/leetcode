class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        major, ref = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == major: ref += 1
            else: ref -= 1
            if ref == 0:
                major, ref = nums[i], 1
        return major
