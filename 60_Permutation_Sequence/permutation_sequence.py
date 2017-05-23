class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans, candidates = "", [i+1 for i in xrange(n)]
        factorial = math.factorial(n - 1)
        k -= 1 # convert to 0 based
        while len(candidates):
            index = k / factorial
            currentDigit = candidates[index]
            ans += str(currentDigit)
            candidates = candidates[:index] + candidates[index + 1:]
            k, n = k % factorial, n - 1
            if n > 0: factorial = math.factorial(n - 1)
        return ans
        
