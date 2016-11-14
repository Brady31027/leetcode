class Solution(object):
    def permuteUnique(self, nums):
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
                for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                    l_tmp = [nums[i]] + j
                    if l_tmp in ll_ans: continue
                    ll_ans.append(l_tmp)
        return ll_ans
