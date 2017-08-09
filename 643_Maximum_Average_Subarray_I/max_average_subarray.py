class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans, total = None, 0.0
        for i in xrange(len(nums)):
            total += nums[i]
            if i >= k: # window overflow
                total -= nums[i - k]
            if i >= k - 1: # window is full
                ans = max(ans, total)
        return ans/float(k)
