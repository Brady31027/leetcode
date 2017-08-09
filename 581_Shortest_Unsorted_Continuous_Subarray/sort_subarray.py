class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tbl = [ unsort == sort for unsort, sort in zip(nums, sorted(nums)) ]
        if all(tbl) == True:
            return 0
        else:
            return len(nums) - tbl.index(False) - tbl[::-1].index(False)
        
