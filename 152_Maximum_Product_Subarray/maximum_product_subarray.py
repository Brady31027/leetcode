class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max_dp = min_dp = nums[0]
        for i in range(1, len(nums)):
            max_dp_tmp = max_dp
            max_dp = max(nums[i], max(max_dp * nums[i], min_dp * nums[i]))
            min_dp = min(nums[i], min(max_dp_tmp * nums[i], min_dp * nums[i]))
            ans = max(max_dp, min_dp, ans)
        return ans
