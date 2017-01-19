class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(candidates, node, target, result, results):
            if len(candidates) < node or node < 2 or candidates[-1] * node < target or candidates[0] * node > target: return
            if node == 2: # basic 2 sum problem
                l, r = 0, len(candidates)-1
                while l < r:
                    if candidates[l]+candidates[r] == target:
                        results.append(result + [candidates[l], candidates[r]])
                        l += 1
                        while l < r and candidates[l] == candidates[l-1]:l += 1
                    elif candidates[l]+candidates[r] < target: l += 1
                    else: r -= 1
            else:
                for i in xrange(len(candidates) - node + 1):
                    if i == 0 or (i > 0 and candidates[i-1] != candidates[i]):
                        dfs(candidates[i+1:], node - 1, target - candidates[i], result+[candidates[i]], results)
          
        results = []  
        nums.sort()
        dfs(nums, 3, 0, [], results) #reduce to 2sum problem
        return results
