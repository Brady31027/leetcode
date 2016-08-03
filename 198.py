class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming
        size = len(nums)
        if size < 1:
            return 0
        odd, even = 0, 0
        for i in range(size):
            if i % 2 == 0:
                odd = max( odd + nums[i], even)
            else:
                even = max (even + nums[i], odd)
        return max(odd, even)
