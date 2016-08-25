class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        nums.sort()
        cnt, prev = 0, None
        for n in nums:
            if n != prev:
                if cnt < 3 and prev != None: return prev
                cnt = 1
            else: cnt += 1
            prev = n
        return nums[-1]
