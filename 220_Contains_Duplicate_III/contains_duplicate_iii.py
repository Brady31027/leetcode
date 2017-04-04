class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket_chain = collections.defaultdict(tuple) # (index, value)
        bucket_width = abs(t) + 1 # to avoid divided by zero
        for i in range(len(nums)):
            bucket_index = nums[i] // bucket_width
            bucket_item = bucket_chain.get(bucket_index)
            left_bucket_item = bucket_chain.get(bucket_index - 1)
            right_bucket_item = bucket_chain.get(bucket_index + 1)
            if (bucket_item and abs(i - bucket_item[0]) <= k and abs(nums[i] - bucket_item[1]) <= t) or \
               (left_bucket_item and abs(i - left_bucket_item[0]) <= k and abs(nums[i] - left_bucket_item[1]) <= t) or \
               (right_bucket_item and abs(i - right_bucket_item[0]) <= k and abs(nums[i] - right_bucket_item[1]) <= t):
                   return True
            else: bucket_chain[bucket_index] = (i, nums[i])
        return False
