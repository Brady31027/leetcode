class Solution(object):
    
    ll_result = []
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None: return []
        self.ll_result = []
        
        def dfs(candidates, target, comb):
            total = sum(comb)
            if total > target: return
            elif total == target:
                self.ll_result.append(comb)
                return
            else:
                for i, v in enumerate(candidates):
                    dfs(candidates[i:], target, comb + [v])
                    
        candidates.sort()
        dfs(candidates, target, [])
        return self.ll_result
                    
