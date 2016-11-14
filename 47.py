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
            prev_anchor = None
            nums.sort()
            for i in xrange(size):
                if prev_anchor == nums[i]: continue
                prev_anchor = nums[i]
                for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                    l_tmp = [nums[i]] + j
                    ll_ans.append(l_tmp)
        return ll_ans
