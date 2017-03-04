class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, len(nums) - 1
        while head < tail:
            sum = nums[head] + nums[tail]
            if sum == target: return [head + 1, tail + 1]
            elif sum > target: tail -= 1
            else: head += 1
        return [0, 0] # we should not come here!
