class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCnt, countTbl = 0, collections.Counter(nums)
        for n in nums:
            if n + 1 in countTbl:
                maxCnt = max(maxCnt, countTbl[n] + countTbl[n + 1] )
        return maxCnt
