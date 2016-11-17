class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        if size == 0: return 0
        elif size == 1: return min(size, citations[0])
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            if size - mid <= citations[mid]: right = mid
            else: left = mid + 1
        return size - left
