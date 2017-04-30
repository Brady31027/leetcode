class NumArray(object):

    treeWidth = None
    binaryIndexedTree = []
    nums = []
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.treeWidth = len(nums)
        self.binaryIndexedTree = [0] * (self.treeWidth + 1)
        # build up BIT
        for i in range(self.treeWidth):
            self.add( i + 1, nums[i])
        
    def getLowestOne(self, x):
        return x & -x
        
    def add(self, i, val):
        while i <= self.treeWidth:
            self.binaryIndexedTree[i] += val
            i += self.getLowestOne(i)
       
    def sum(self, i):
        total = 0
        while i > 0: # go left
            total += self.binaryIndexedTree[i]
            i -= self.getLowestOne(i)
        return total

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add( i + 1, val - self.nums[i] )
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return 0
        return self.sum(j + 1) - self.sum(i)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
