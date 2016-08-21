
from itertools import combinations

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ll_result = []
        ll_candidates = [sorted(list(comb)) for comb in combinations(nums, 4) if sum(comb) == target ]
        for l_c in ll_candidates:
            if l_c in ll_result: continue
            else: ll_result.append(l_c)
        return ll_result
