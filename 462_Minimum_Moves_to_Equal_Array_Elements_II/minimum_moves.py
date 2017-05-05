class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[ len(nums) / 2 ]
        moveCount = 0
        for num in nums:
            moveCount += abs(num - median)
        return moveCount
