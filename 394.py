class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num, l_stack = 0, [["", 1]]
        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c == '[':
                l_stack.append(["", num])
                num = 0
            elif c == ']':
                pattern, repeat = l_stack.pop()
                l_stack[-1][0] += pattern * repeat
            else: l_stack[-1][0] += c
        return l_stack[0][0]
