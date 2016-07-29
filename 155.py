class MinStack(object):

    l_stack = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.l_stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.l_stack) > 0:
            self.l_stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.l_stack) > 0:
            return self.l_stack[ len(self.l_stack) - 1 ]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.l_stack) > 0:
            l_sorted_stack = sorted(self.l_stack)
            return l_sorted_stack[0]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
