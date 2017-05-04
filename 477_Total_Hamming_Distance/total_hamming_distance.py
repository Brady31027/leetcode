from itertools import combinations

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getHammingDistance(a, b):
            return bin(a ^ b)[2:].count('1')
        
        totalHamming = 0 
        for comb in itertools.combinations(nums, 2):
            totalHamming += getHammingDistance(comb[0], comb[1])
        return totalHamming
