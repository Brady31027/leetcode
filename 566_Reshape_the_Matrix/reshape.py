class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        newMat = [[0 for _ in xrange(c)] for _ in xrange(r)]
        oriRow, oriCol = len(nums), len(nums[0])
        if r * c != oriRow * oriCol: return nums
        for row in xrange(oriRow):
            for col in xrange(oriCol):
                order = row * oriCol + col
                newMat[order / c][order % c] = nums[row][col]
        return newMat
                
        
