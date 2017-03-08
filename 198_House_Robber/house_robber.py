class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        init: state[0] = money[0]
              state[1] = max(state[0], moeny[1])
        function: state[n] = max(money[n] + state[n - 2], money[n-1])
        """
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])
        state = [0] * len(nums)
        state[0], state[1] = nums[0], max(nums[0],nums[1])
        for i in range(2, len(nums)):
            state[i] = max(state[i-1], state[i-2]+nums[i])
        return state[-1]
