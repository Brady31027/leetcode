class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums[0] > target: return 0
        if nums[-1] < target: return len(nums) 
        local_min, local_max = 0, len(nums)
        idx = (local_min + local_max)//2
        prev_result, cur_result, prev_idx = 0,0,-1
        
        while nums[idx] != target:
            if nums[idx] > target: # move left half, guess too large
                local_max = idx
                cur_result = 1
            else: # move right half, guess to small
                local_min = idx
                cur_result = 0
            if abs(idx - prev_idx) == 1 and (cur_result ^ prev_result) == 1: return max(idx, prev_idx)
            prev_result, prev_idx = cur_result, idx
            idx = (local_min + local_max) // 2
        return idx  
