class Solution(object):
    
    """
    input : 1, 2, 3, 4, 5 (k = 3)
    output: 3, 4, 5, 1, 2
    another algorithm:
      (1) reverse second half: 1, 2, 5, 4, 3
      (2) reverse first half : 2, 1, 5, 4, 3
      (3) reverse all: 3, 4, 5, 1, 2
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp, k = list(nums), k % len(nums) # deep copy nums to tmp
        for i in xrange( len(nums) ):
            nums[ ( i + k ) % len(nums) ] = tmp[i]
