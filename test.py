class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l_uniset = list(set(nums1) & set(nums2))
        l_result = []
        for i in l_uniset:
            cnt1 = nums1.count(i)
            cnt2 = nums2.count(i)
            repeat_cnt = cnt1 if cnt1 <= cnt2 else cnt2
            for j in range(repeat_cnt):
                l_result.append(i)
        return l_result 
