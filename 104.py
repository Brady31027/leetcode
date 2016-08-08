# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        node = root
        if node.left is None and node.right is None:           return 1
        elif node.left is None and node.right is not None:     return self.maxDepth(node.right) + 1
        elif node.left is not None and node.right is None:     return self.maxDepth(node.left) + 1
        elif node.left is not None and node.right is not None: return max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1
