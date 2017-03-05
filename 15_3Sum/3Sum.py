class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l_ans = []
        
        def two_sum(numbers, target):
            if len(numbers) < 2 or numbers[-1] * 2 < -target or numbers[0] * 2 > -target: return None
            head, tail = 0, len(numbers) - 1
            l_candidates = []
            while head < tail:
                sum = numbers[head] + numbers[tail]
                if sum == -target:
                    l_candidates.append( [ target, numbers[head], numbers[tail] ] )
                    head += 1
                    while head < tail and numbers[head] == numbers[head - 1 ]:
                        head += 1
                elif sum > -target:
                    tail -= 1
                else:
                    head += 1
            return l_candidates
                    
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                ans = two_sum(nums[i+1: len(nums)], nums[i])
                if ans is not None : l_ans += ans
        return l_ans
