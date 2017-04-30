class NumArray(object):

    arrSum = []
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arrSum = []
        localSum = 0
        for i in nums:
            localSum += i
            self.arrSum.append( localSum )

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0: return self.arrSum[j]
        return self.arrSum[j] - self.arrSum[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
