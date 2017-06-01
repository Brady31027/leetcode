class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq, ans = collections.deque(), []
        for i, v in enumerate(nums):
            while dq and nums[ dq[-1] ] < v: dq.pop()
            dq.append(i)
            if i - dq[0] == k: dq.popleft()
            if i >= k - 1: ans.append(nums[dq[0]])
        return ans
                
            
            
