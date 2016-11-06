class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0: return 0
        elif size == 1: return 1
        l_len = [1] * size
        for i in xrange(size):
            for j in xrange(i+1, size):
                if nums[j] > nums[i]: l_len[j] = max(l_len[j], l_len[i]+1)
        l_len.sort()
        return l_len[-1]
