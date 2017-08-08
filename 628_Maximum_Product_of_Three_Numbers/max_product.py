class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = heapq.nlargest(3, nums)
        negative = heapq.nsmallest(2, nums)
        return max(positive[0] * positive[1] * positive[2], 
                   negative[0] * negative[1] * positive[0])
