class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N: return
            if N == 2: # two pointers solve sorted 2-sum problem
                left,right = 0, len(nums)-1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
            else: # recursively reduce N
                for i in xrange(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        nums.sort()
        findNsum(nums, target, 4, [], results)
        return results
