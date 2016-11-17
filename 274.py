class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_idx = 0
        citations.sort(reverse=True)
        for i, v in enumerate(citations):
            if (i+1) <= v: h_idx = max(h_idx, i+1)
        return h_idx
