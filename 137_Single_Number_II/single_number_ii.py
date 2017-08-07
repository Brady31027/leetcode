class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ( sum(set(nums)) * 3 - sum(nums) ) / 2
        """
        ans = 0
        for i in xrange(32):
            sum = 0
            for n in nums:
                if n >> i & 1:
                    sum += 1
            sum %= 3
            ans |= (sum << i)
        if ans > 0x7FFFFFFF:
            return -int(0x100000000 - ans)
        return ans
        """
