class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = []
        for k, v in enumerate(nums):
            sort.append((v, k))
        sort.sort(reverse=True)
        size = len(nums)
        for i, (score, index) in enumerate(sort):
            if i == 0: nums[index] = "Gold Medal"
            elif i == 1: nums[index] = "Silver Medal"
            elif i == 2: nums[index] = "Bronze Medal"
            else: nums[index] = str(i+1)
        return nums
