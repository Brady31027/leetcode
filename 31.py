class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #http://www.cnblogs.com/zuoyuan/p/3780167.html
        anchor, size = -1, len(nums)
        if size < 2: return
        if size == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        # find anchor
        for i in xrange(size-1, 0, -1):
            if nums[i] > nums[i-1]:
                anchor = i-1
                break
        # no anchor, reverse nums
        if anchor == -1: nums.sort()
        else:
            # swap ancher and the first number which is greater than anchor from tail
            for i in xrange(size-1, anchor, -1):
                if nums[i] > nums[anchor]:
                    nums[i], nums[anchor] = nums[anchor], nums[i]
                    break
            # reverse range from anchor+1 to tail
            left, right = anchor + 1, size -1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
