class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            cnt = sum( num <= mid for num in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low
