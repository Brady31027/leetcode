class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, total, minLen = 0, 0, len(nums) + 1
        for i in xrange(len(nums)):
            total += nums[i]
            while total >= s:
                minLen = min(minLen, i - start + 1)
                total -= nums[start]
                start += 1
        return minLen if minLen != len(nums)+1 else 0
        
