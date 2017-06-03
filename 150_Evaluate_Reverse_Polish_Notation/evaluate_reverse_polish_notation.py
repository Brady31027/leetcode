class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        opsTbl = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        for op in tokens:
            if op in opsTbl:
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append( int(opsTbl[op](operand1 * 1.0, operand2)))
            else:
                stack.append(int(op))
        return stack[-1]
