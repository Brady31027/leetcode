class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        third, secondStack = float('-inf'), []
        nums.reverse()
        for i in xrange(len(nums)):
            if nums[i] < third: return True
            while secondStack and nums[i] > secondStack[-1]:
                third = secondStack.pop()
            secondStack.append(nums[i])
        return False
            
