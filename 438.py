class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l_ans = []
        l_p_permutations = list(itertools.permutations(p, len(p)))
        for pattern in l_p_permutations:
            str_pattern = "".join(pattern)
            l_idx = [m.start() for m in re.finditer(str_pattern, s)]
            for idx in l_idx: l_ans.append(idx)
        return l_ans
