class Queue(object):
    l_queue = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.l_queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.l_queue) > 0:
            self.l_queue.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.l_queue) > 0:
            return self.l_queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.l_queue) == 0 else False
