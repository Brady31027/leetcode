class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ll_ans = []
        for t_permutation in itertools.permutations(nums):
            l_ans = list(t_permutation)
            if l_ans not in ll_ans: ll_ans.append(l_ans)
        return ll_ans
