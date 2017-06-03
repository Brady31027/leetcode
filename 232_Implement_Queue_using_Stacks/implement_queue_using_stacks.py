class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stackA = []
        self._stackB = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._stackA.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self._stackB.pop()
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self._stackB:
            while self._stackA:
                self._stackB.append(self._stackA.pop())
        return self._stackB[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if not self._stackA and not self._stackB else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
