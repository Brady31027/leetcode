class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        memo = collections.defaultdict(int)
        for i in range(len(nums)):
            existed_index = memo.get(nums[i])
            if existed_index is not None and i - existed_index <= k: return True
            else: memo[nums[i]] = i
        return False
