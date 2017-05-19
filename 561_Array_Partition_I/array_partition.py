class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in xrange(0, len(nums), 2):
            ans += nums[i]
        return ans
