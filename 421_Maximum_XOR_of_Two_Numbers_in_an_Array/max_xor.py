from itertools import combinations

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxXor = 0
        for comp in itertools.combinations(nums, 2):
            maxXor = max(comp[0] ^ comp[1], maxXor)
        return maxXor
