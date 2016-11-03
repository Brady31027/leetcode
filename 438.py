class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l_ans, ls, lp = [], len(s), len(p)
        cp = collections.Counter(p)
        cs = collections.Counter()
        for i in xrange(ls):
            cs[s[i]] += 1
            if i >= lp:
                cs[s[i-lp]] -= 1
                if cs[s[i-lp]] <= 0: del cs[s[i-lp]]
            if cp == cs: l_ans.append(i - lp + 1)
        return l_ans
