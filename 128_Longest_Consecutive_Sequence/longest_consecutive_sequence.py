class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, tbl = 0, collections.defaultdict(int)
        for n in nums:
            if not tbl.get(n):
                tbl[n], left, right = 1, tbl.get(n-1, 0), tbl.get(n+1, 0)
                boundary = left + right + 1
                result = max(result, boundary)
                tbl[ n - left] = tbl[ n + right] = boundary
        return result
