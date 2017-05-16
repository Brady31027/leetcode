class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = nums[0], nums[nums[0]]
        while fast != slow:
            slow = nums[ slow ]
            fast = nums[ nums[ fast ] ]
        fast = 0
        while fast != slow:
            fast = nums[ fast ]
            slow = nums[ slow ]
        return slow
