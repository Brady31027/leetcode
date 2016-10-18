from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l_ans, ll_ans = [], []
        for i in xrange(0, len(nums)+1):
            l_ans = list(itertools.combinations(nums, i))
            for t in l_ans: ll_ans.append(list(t))
        return ll_ans
 
