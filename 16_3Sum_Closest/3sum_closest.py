class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def two_sum(pivot, nums, target):
            if len(nums) < 2: return None
            head, tail, min_dis, ret_sum = 0, len(nums) - 1, 2147483647, 0
            while head < tail:
                sum = pivot + nums[head] + nums[tail]
                if  sum == target:
                    return sum
                elif sum > target:
                    tail -= 1
                else:
                    head += 1
                dis = abs(target - sum)
                if dis < min_dis:
                    ret_sum = sum
                    min_dis = dis
            return ret_sum
            
        nums.sort()
        closest_sum, min_dis = target, 2147483647
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                sum = two_sum(nums[i], nums[i+1:], target)  
                if sum is not None and abs(target - sum) < min_dis: 
                    closest_sum = sum
                    min_dis = abs(target - sum)
        return closest_sum
