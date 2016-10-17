class Solution(object):
    MIN_INT = -(2**31)
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2: return 0
        size = len(A)
        ans = self.MIN_INT
        for sft in range(size):
            tmp_ans = 0
            for i in range(1, size):
                tmp_ans += i * A[ (i+sft) % size]
            if tmp_ans > ans: ans = tmp_ans
        return ans
