# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev, l_stack = -9999999999999, []
        while root or l_stack:
            if root:
                l_stack.append(root)
                root = root.left
            else:
                root = l_stack.pop()
                if prev >= root.val: return False
                prev = root.val
                root = root.right
        return True
            
