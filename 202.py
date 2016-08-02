class Solution(object):
    def isHappy(self, n):
        cnt = 0
        LIMIT = 30
        """
        :type n: int
        :rtype: bool
        """
        result = True
        while n != 1:
            if cnt > LIMIT:
                result = False
                break
            str_n = str(n)
            n = 0
            for c in str_n:
                i_char = int(c) ** 2
                n += i_char
                cnt += 1
        return result
