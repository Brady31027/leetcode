class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        ans = [0] * ( len(num1) + len(num2) )
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])
                ans[i + j + 1] += ans[i + j] / 10
                ans[i + j] = ans[i + j] % 10
        head, tail = 0, len(ans) - 1
        while head <= tail:
            ans[head], ans[tail] = str(ans[tail]), str(ans[head])
            head, tail = head + 1, tail - 1
        product = "".join(ans).lstrip('0')
        return product or "0"
