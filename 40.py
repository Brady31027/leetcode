class Solution(object):
    ll_ans = []
    def dfs(self, candidates, target, start, l_ans):
        if target == 0 and l_ans not in self.ll_ans: return self.ll_ans.append(l_ans)
        for i in xrange(start, len(candidates)):
            if i != start and candidates[i] == candidates[i-1]: continue # ?? why ??
            if candidates[i] > target: return
            self.dfs(candidates, target - candidates[i], i + 1, l_ans + [candidates[i]])
            
    def combinationSum2(self, candidates, target):
        if target == 0: return [[]]
        self.ll_ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.ll_ans
