class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq, ans = collections.deque(maxlen=k), []
        for n in nums:
            dq.append(n)
            if len(dq) > k - 1:
                ans.append(max(dq))
        if not ans and dq: ans.append(max(dq))
        return ans
        
