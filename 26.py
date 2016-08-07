class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, set_book = 0, set()
        for n in nums:
            if n not in set_book:
                nums[idx] = n
                idx += 1
                set_book.add(n)
        return idx
