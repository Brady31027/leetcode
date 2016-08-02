class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # early rejection
        if len(nums) == len(set(nums)) or k == 0:
            return False
        dict_nums = {}
        for i in range( len(nums) ):
            if nums[i] in dict_nums:
                if i - dict_nums[ nums[i] ] <= k:
                    return True
            dict_nums[ nums[i] ] = i
        return False
            
