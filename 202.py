class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist = {n}
        while n != 1:
            ans, d = 0, n
            while d > 0:
                d, r = divmod(d, 10)
                ans += (r ** 2)
            if ans in exist: return False
            exist.add(ans)
            n = ans
        return True
