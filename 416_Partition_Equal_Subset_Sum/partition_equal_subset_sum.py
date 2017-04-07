class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #backpack
        total = sum(nums)
        if total % 2 != 0: return False
        total //= 2
        dp = [1] + [0] * total
        for n in nums:
            for i in range(total, n - 1, -1):
                dp[i] |= dp[i - n]
        return dp[ total ] == 1
