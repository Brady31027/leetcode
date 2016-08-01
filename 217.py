class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        existed_set = set()
        for i in nums:
            if i in existed_set:
                return True
            else:
                existed_set.add(i)
        return False
        # using count(x) may not be a good performance solution
        """
        for i in nums:
            if nums.count(i) > 1:
                return True
        return False
        """
