class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        intersectionSet = set(nums1) & set(nums2)
        for element in intersectionSet:
            repeatCnt = min(nums1.count(element), nums2.count(element))
            ans += [element] * repeatCnt
        return ans
