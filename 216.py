class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, node, l_result, ll_result):
            if len(candidates) < node or node < 2 or candidates[0] * node > target or candidates[-1] * node < target:
                return #early rejection
            elif node == 2: # basic 2 sum problem
                l, r = 0, len(candidates)-1
                while l < r:
                    if candidates[l] + candidates[r] == target:
                        ll_result.append(l_result + [candidates[l], candidates[r]])
                        l += 1 # very important to get another answer
                    elif candidates[l] + candidates[r] > target: r -= 1
                    else: l += 1
            else:
                for i in xrange(len(candidates) - node + 1):
                    dfs(candidates[i+1:], target - candidates[i], node - 1, l_result + [candidates[i]], ll_result)
            
        ll_result = []
        candidates = [1,2,3,4,5,6,7,8,9]
        dfs(candidates, n, k, [], ll_result)
        return ll_result
                    
        
