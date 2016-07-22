
from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for comb in combinations(nums, 2):
            if comb[0] + comb[1] == target:
                first, second = nums.index(comb[0]), nums.index(comb[1])
                if first != second:
                    return [first, second]
                else:
                    nums.remove(comb[0])
                    return [first, nums.index(comb[1])+1]
