
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l_result = []
        for c in permutations(nums, len(nums)):
            l_result.append(list(c))
        return l_result
        
