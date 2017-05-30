class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in xrange(n - 1):
            cnt, prev, tmp = 1, None, ""
            for j in xrange(len(ans) + 1): # for the last token
                if j == len(ans) or ans[j] != prev:
                    if prev: tmp += str(cnt) + prev
                    prev = ans[j] if j < len(ans) else None
                    cnt = 1
                else:
                    cnt += 1
            ans = tmp
        return ans
            
        
