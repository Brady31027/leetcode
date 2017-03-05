class Solution(object):
    def fourSum(self, nums, target):
        
        def two_sum(existed_nums, numbers, target):
            if len(numbers) < 2 or numbers[0] * 2 > target or numbers[-1] * 2 < target: return None
            head, tail, l_candidates = 0, len(numbers) - 1, []
            while head < tail:
                if numbers[head] + numbers[tail] == target:
                    l_candidates.append(existed_nums + [ numbers[head], numbers[tail] ] )
                    head += 1
                    while head < tail and numbers[head] == numbers[head - 1]: head += 1
                elif numbers[head] + numbers[tail] > target:
                    tail -= 1
                else:
                    head += 1
            return l_candidates
        
        l_ans = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                for j in range(i+1, len(nums)):
                    if (j == i + 1) or ((j > i + 1) and (nums[j] != nums[j - 1])):
                        ans = two_sum([nums[i], nums[j]], nums[j+1: len(nums)], target - nums[i] - nums[j])
                        if ans is not None: l_ans += ans
        return l_ans
