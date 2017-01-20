class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, max_cnt = 0, 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt > max_cnt: max_cnt = cnt
        return max_cnt
