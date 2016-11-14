class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size == 0: return []
        elif size == 1: return [nums]
        else:
            ll_ans = []
            for i in xrange(size):
                for j in self.permute(nums[:i] + nums[i+1:]):
                    ll_ans.append([nums[i]]+j)
        return ll_ans
