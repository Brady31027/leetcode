class MinStack(object):

    l_stack, l_min_stack = [], []
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_stack = []
        self.l_min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.l_min_stack) == 0 or x <= self.l_min_stack[-1]:
            self.l_min_stack.append(x)
        self.l_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.getMin():
            self.l_min_stack.pop()
        self.l_stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        #better to have empty handling
        return self.l_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # better to have empty handling
        return self.l_min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
