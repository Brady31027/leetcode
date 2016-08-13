ass Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #[version 2]
        while n > 0:
            if m <= 0 or nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                #nums1[m - 1] = nums2[n - 1] # no need, will be overwirte later
                m -= 1
                
        # [version 2]
        """
        nums1[m:n+m] = nums2[:n]
        nums1.sort()
        """
        # [version 1]
        """
        for i in range(n): nums1[m + i] = nums2[i]
        nums1.sort()
        """
