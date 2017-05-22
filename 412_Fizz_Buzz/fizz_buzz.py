class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [ str(i) for i in xrange(1, n + 1) ]
        fizz, buzz, fizzbuzz = 3, 5, 15
        while fizz <= n or buzz <= n:
            if fizz <= n:
                ans[fizz - 1] = "Fizz"
                fizz += 3
            if buzz <= n:
                ans[buzz - 1] = "Buzz"
                buzz += 5
        while fizzbuzz <= n:
            if fizzbuzz <= n:
                ans[fizzbuzz - 1] = "FizzBuzz"
                fizzbuzz += 15
        return ans
