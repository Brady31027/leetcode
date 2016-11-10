class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        size, cnt = len(nums), 0
        nums.sort()
        while len(set(nums)) > 1:
            for i in xrange(size-1):
                nums[i] += 1
            cnt += 1
            nums.sort()
        return cnt
