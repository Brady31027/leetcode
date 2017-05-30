class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i, j in itertools.combinations(xrange(1, n), 2):
            a, b = num[:i], num[i:j]
            # remove leading 0s
            if str(int(a)) != a or str(int(b)) != b: continue
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n: return True
        return False
            
        
