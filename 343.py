#https://discuss.leetcode.com/topic/43055/why-factor-2-or-3-the-math-behind-this-problem/2
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        result, l_result_from_0_to_10 = 1, [0,0,1,2,4,6,9,12,18,27,36]
        while n > 10: result, n = result*3, n-3
        return result * l_result_from_0_to_10[n]
