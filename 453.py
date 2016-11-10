class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        size, cnt = len(nums), 0
        min_val = min(nums)
        for n in nums:
            cnt += (n - min_val)
        return cnt
