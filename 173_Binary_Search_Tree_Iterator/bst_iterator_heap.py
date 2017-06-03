# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.heap, self.queue = [], []    
        if root:
            self.heap, self.queue = [], [root]
            while self.queue:
                node = self.queue.pop(0)
                heapq.heappush(self.heap, node.val)
                if node.left: self.queue.append(node.left)
                if node.right:self.queue.append(node.right)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.heap else False
        

    def next(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.heap)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
