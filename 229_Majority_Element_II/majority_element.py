class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major1, major2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == major1: count1 += 1
            elif n == major2: count2 += 1
            elif count1 == 0: major1, count1 = n, 1
            elif count2 == 0: major2, count2 = n, 1
            else: count1, count2 = count1 - 1, count2 - 1
        return [ m for m in [major1, major2] if m is not None and nums.count(m) > len(nums)//3]
