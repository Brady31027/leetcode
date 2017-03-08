class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        if nums[0] == 0: return False
        target = len(nums) - 1
        state = [0] * target
        state[0] = nums[0]
        for i in range(1, len(state)):
            state[i] = max(state[i-1]-1, nums[i])
            if state[i] == 0: return False
        return True if state[-1] > 0 else False
