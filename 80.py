class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return len(nums)
        i, length, prev1, prev2 = 2, len(nums), nums[0], nums[1]
        while i < length:
            if nums[i] < prev1 or nums[i] < prev2: break
            if nums[i] == prev1 and nums[i] == prev2:
                nums.append(nums[i])
                del nums[i]
                i-= 1
                length -= 1
            if nums[i] != prev1:
                prev1 = nums[i]
            elif nums[i] != prev2:
                prev2 = nums[i]
            i += 1
        return length
