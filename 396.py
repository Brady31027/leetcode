class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2: return 0
        size, sums = len(A), sum(A)
        total = sum( i*v for i,v in enumerate(A))
        ans = total
        for x in range(size - 1,0,-1):
            total += sums - size * A[x]
            ans = max(ans, total)
        return ans
