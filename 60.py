class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l_input = [i+1 for i in xrange(n)]
        s_ans = ''
        def generatePermute(l_nums):
            size = len(l_nums)
            if size == 0: return []
            elif size == 1: return [l_nums]
            else:
                ll_ans = []
                for i in xrange(size):
                    for j in generatePermute(l_nums[:i]+l_nums[i+1:]):
                        ll_ans.append([l_nums[i]]+j)
            return ll_ans
        ll_ans = generatePermute(l_input)
        for n in ll_ans[k-1]: s_ans += str(n)
        return s_ans
            
        
        
