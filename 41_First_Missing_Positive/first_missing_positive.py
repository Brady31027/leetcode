class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        arr = [0] * size
        for n in nums:
            if n < 1 or n > size:
                continue
            arr[n-1] = n
        for i in xrange(size):
            if arr[i] == 0:
                return i + 1
        return size + 1
            
