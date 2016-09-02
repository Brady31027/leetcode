from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(comb) for comb in combinations([i for i in range(1, n+1)], k)]
       
