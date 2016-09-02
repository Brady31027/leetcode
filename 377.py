#https://discuss.leetcode.com/topic/52542/c-template-for-all-combination-problem-set
#https://discuss.leetcode.com/topic/52302/1ms-java-dp-solution-with-detailed-explanation
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0: return 1
        comb = 0
        for i in xrange(len(nums)):
            if target >= nums[i]:
                comb += self.combinationSum4(nums, target - nums[i])
        return comb
