class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum_for_each_bit( how many 0's * how many 1's)
        ans = 0
        for oft in range(32):
            mask = 1 << oft
            oneCnt, zeroCnt = 0, 0
            for number in nums:
                if number & mask:
                    oneCnt += 1
                else:
                    zeroCnt += 1
            ans += (oneCnt * zeroCnt)
        return ans
        
