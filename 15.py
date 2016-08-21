
from itertools import combinations

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ll_result = []
        ll_candidates = [sorted(list(comb)) for comb in combinations(nums, 3) if sum(comb) == 0 ]
        for l_c in ll_candidates:
            if l_c in ll_result: continue
            else: ll_result.append(l_c)
        return ll_result
