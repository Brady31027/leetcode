class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        r, v = "", "aeiouAEIOU"
        l_return = []
        l_v_in_s = [ c for c in s if c in v]
        for c in s:
            if c in v:
                l_return.append(l_v_in_s.pop())
            else:
                l_return.append(c)
        return r.join(l_return)
