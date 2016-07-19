class NumArray(object):
    l_sum = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        sum = 0
        self.l_sum = []
        for i in nums:
            sum += i
            self.l_sum.append(sum)
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.l_sum[j] - self.l_sum[i-1]
        else:
            return self.l_sum[j]
