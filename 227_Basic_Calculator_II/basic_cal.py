class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return '0'
        stack, num, op, s = [], 0, "+", re.sub(r'\s', '', s)
        for c in s + " ":
            if c.isdigit():
                num = 10 * num + int(c)
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append( stack.pop() * num )
                else:
                    stack.append( (int) ((float)(stack.pop()) / num))
                op, num = c, 0
        return sum(stack)
            
            
