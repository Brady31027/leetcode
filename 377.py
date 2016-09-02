#https://discuss.leetcode.com/topic/52542/c-template-for-all-combination-problem-set
#https://discuss.leetcode.com/topic/52302/1ms-java-dp-solution-with-detailed-explanation
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target):
            if dp[target] != -1: return dp[target]
            comb = 0
            for i in xrange(len(nums)):
                if nums[i] <= target:
                    comb += helper(nums, target - nums[i])
            dp[target] = comb
            return comb
            
        if target == 0: return 1
        dp = [-1] * (target + 1)
        dp[0] = 1
        comb = helper(nums, target)
        return comb
