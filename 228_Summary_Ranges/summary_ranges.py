class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) < 2: return [ str(n) for n in nums]
        start, end, ans = nums[0], nums[0], []
        for i in xrange(1, len(nums) + 1): # +1 is tricky for the last range
            if i < len(nums) and nums[i] - nums[i-1] == 1:
                end = nums[i]
            else:
                if start != end:
                    ans.append(str(start)+"->"+str(end))
                else:
                    ans.append(str(end))
                if i < len(nums):
                    start = end = nums[i]
        return ans
