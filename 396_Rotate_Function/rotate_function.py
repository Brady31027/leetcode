class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2: return 0
            
        unweightedSum, lenA = sum(A), len(A)
        originalWeightedSum = 0
        for k, v in enumerate(A):
            originalWeightedSum += (k * v)
        ans = newAns = originalWeightedSum
        for i in xrange(lenA - 1, 0, -1): # no need to run 0 -> no-rotate
            newAns += unweightedSum - A[i] * lenA
            ans = max(ans, newAns)
        return ans
