class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        if size < 3 : return 0
        ans, cnt = 0, 0
        for i in xrange(2, size):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                cnt += 1
                ans += cnt
            else: cnt = 0
        return ans
