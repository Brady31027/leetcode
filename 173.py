# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    idx, l_ans, l_stack = 0, [], []
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.idx, self.l_ans, self.l_stack = 0, [], []
        while root or self.l_stack:
            if root:
                self.l_stack.append(root)
                root = root.left
            else:
                root= self.l_stack.pop()
                self.l_ans.append(root.val)
                root = root.right

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.idx < len(self.l_ans) else False
        

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.l_ans[self.idx - 1]
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
