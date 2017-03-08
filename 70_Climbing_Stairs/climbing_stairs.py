class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4: return n # shortcut
        ways, prev_ways, prev2_ways, stair = 3, 2, 1, 3
        while stair <= n:
            ways = prev_ways + prev2_ways
            prev2_ways, prev_ways = prev_ways, ways
            stair += 1
        return ways
