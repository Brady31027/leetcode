
from itertools import combinations

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l_ans = []
        l_filtered_input = sorted([x for x in candidates if x <= target])
        for i in range(len(l_filtered_input)):
            for comb in combinations(l_filtered_input, i):
                total = sum(comb)
                if total > target: break
                elif total == target: l_ans.append(list(comb))
        return l_ans
