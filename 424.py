class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict_c = collections.Counter()
        start, end, ans = 0, 0, 0
        while end < len(s):
            dict_c[s[end]] += 1
            end += 1
            while end - start - max(dict_c.values()) > k:
                dict_c[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans
