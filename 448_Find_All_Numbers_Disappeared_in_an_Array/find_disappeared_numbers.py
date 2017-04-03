class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        indices = set()
        values = set()
        for i, v in enumerate(nums):
            indices.add(i+1)
            values.add(v)
        return list(indices - values)
        
