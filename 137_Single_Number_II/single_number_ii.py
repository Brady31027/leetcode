class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # early reject for [x] or [x, x]
        if len(nums) < 3: return nums[0]
        
        nums.sort()
        prevNumber, repeatCount = None, 0
        for n in nums:
            if n != prevNumber:
                if repeatCount < 3 and prevNumber is not None:
                    return prevNumber
                # reset counter
                repeatCount = 1
            else:
                repeatCount += 1
            prevNumber = n
        return nums[-1]
