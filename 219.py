class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_book = {}
        for i in range(len(nums)):
            if nums[i] in dict_book.keys():
                if i - dict_book.get(nums[i]) <= k:
                    return True
                else:
                    dict_book[nums[i]] = i
            else:
                dict_book[nums[i] ] = i
        return False
        
