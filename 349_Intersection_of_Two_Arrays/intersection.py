class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # lazy approach
        # return list(set(nums1).intersection(nums2))
        ans = []
        set1, set2 = set(nums1), set(nums2)
        for element in set1:
            if element in set2: ans.append(element)
        return ans
