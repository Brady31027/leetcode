
#https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration/2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        elif len(nums) == 1: return [ nums[0] ]
        elif len(nums) == 2: return [ nums[0], nums[1] ] if nums[0] != nums[1] else [ nums[0] ]
        
        cnt1, cnt2, major1, major2 = 0,0,nums[0],nums[1]
        for n in nums:
            if n == major1: cnt1 += 1
            elif n == major2: cnt2 += 1
            elif cnt1 == 0: major1, cnt1 = n, 1
            elif cnt2 == 0: major2, cnt2 = n, 1
            else: cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        if major1 == major2: return [major1]
        return [n for n in (major1, major2) if nums.count(n) > len(nums)//3 ]
