class Stack(object):
    l_stack = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.l_stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        #use del if faster?  
        #self.l_stack.pop( len(self.l_stack) - 1 )
        del self.l_stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.l_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if len(self.l_stack) > 0 else True
