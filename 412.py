class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l_ans = []
        for i in xrange(1, n+1, 1):
            if i % 15 == 0: l_ans.append("FizzBuzz")
            elif i % 5 == 0: l_ans.append("Buzz")
            elif i % 3 == 0: l_ans.append("Fizz")
            else: l_ans.append(str(i))
        return l_ans
