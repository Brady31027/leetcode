class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0 if len(nums) == 0 else nums[0]
            
        def rob_linear(nums):
            if len(nums) < 2: return 0 if len(nums) == 0 else nums[0]
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[-1]
            
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]) )
