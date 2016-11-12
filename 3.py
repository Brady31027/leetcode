class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_c, start, end, max_len = {}, 0, 0, 0
        for c in s:
            end += 1
            dict_c[c] = dict_c.get(c, 0) + 1
            while dict_c[c] > 1:
                dict_c[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
