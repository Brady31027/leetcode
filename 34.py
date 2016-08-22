class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or nums[0] > target or nums[-1] < target: return [-1, -1]
        local_min, local_max = 0, len(nums)
        idx = (local_min + local_max)//2
        prev_result, cur_result, prev_idx = 0,0,-1
        
        while nums[idx] != target:
            if nums[idx] > target:
                local_max = idx
                cur_result = 1
            else: 
                local_min = idx
                cur_result = 0
            if abs(idx - prev_idx) == 1 and (cur_result ^ prev_result) == 1: return [-1, -1]
            prev_result, prev_idx = cur_result, idx
            idx = (local_min + local_max)//2
        
        l_ans = [idx, idx]
        tmp = idx
        while tmp >= 0 and nums[tmp] == target:
            l_ans[0] = tmp
            tmp -= 1
        for i in range(idx, len(nums), 1): #right
            if nums[i] == target: l_ans[1] = i
            else: break
            
        return l_ans
