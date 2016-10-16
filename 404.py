# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l_children = [root]
        sum = 0
        while l_children:
            node = l_children.pop(0)
            if node is not None and node.left is not None:
                l_children.append(node.left)
                if node.left.left is None and node.left.right is None: sum += node.left.val
            if node is not None and node.right is not None: l_children.append(node.right)
        return sum
