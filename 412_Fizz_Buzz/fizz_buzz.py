class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for num in xrange(1, n + 1):
            if num % 15 == 0: ans.append("FizzBuzz")
            elif num % 5 == 0: ans.append("Buzz")
            elif num % 3 == 0: ans.append("Fizz")
            else: ans.append(str(num))
        return ans
