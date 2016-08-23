
from itertools import combinations
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l_ans = []
        l_candidates = [x for x in candidates if x <= target]
        l_candidates.sort()
        for i in range(len(l_candidates)+1):
            for c in combinations(l_candidates, i):
                total = sum(c)
                if total == target and list(c) not in l_ans: l_ans.append(list(c))
        return l_ans
        
