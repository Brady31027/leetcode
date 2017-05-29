class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1Len, num2Len, carry, total = len(num1), len(num2), 0, 0
        ans = []
        while num1Len or num2Len or carry:
            total = carry
            if num1Len > 0:
                num1Len -= 1
                total += int(num1[num1Len])
            if num2Len > 0:
                num2Len -= 1
                total += int(num2[num2Len])
            carry = total / 10
            ans.append(str(total % 10))
        return "".join(reversed(ans))
                
            
