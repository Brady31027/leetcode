class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2: return 0 if size == 0 else 1
        dp = [0] * size
        positive_diff = None
        for i in range(1, size):
            if nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
                continue
            local_positive_diff = nums[i] > nums[i-1]
            dp[i] = dp[i-1] + 1 if local_positive_diff != positive_diff else dp[i-1]
            positive_diff = local_positive_diff
        return dp[-1] + 1
