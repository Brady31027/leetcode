class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = None
        self._stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._stack:
            val = x - self._min
            self._stack.append(val)
            if val < 0:
                self._min = x
        else:
            self._stack.append(0)
            self._min = x
            
        

    def pop(self):
        """
        :rtype: void
        """
        val = self._stack.pop()
        if val < 0:
            self._min = self._min - val
        

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1] + self._min if self._stack[-1] > 0 else self._min

    def getMin(self):
        """
        :rtype: int
        """
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
