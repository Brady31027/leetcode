class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        tbl = collections.Counter() # hash of {char: repeat_cnt}
        start, end, ans = 0, 0, 0
        while end < len(s):
            tbl[ s[end] ] += 1
            end += 1
            while end - start - max(tbl.values()) > k:
                tbl[ s[start] ] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans
        
