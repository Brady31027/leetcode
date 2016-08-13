# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        # Top-Down recusion: straight forward 
        if root is None: return True
        
        def getDepth(root):
            return 0 if root == None else max(getDepth(root.left), getDepth(root.right)) + 1
        
        return True if abs( getDepth(root.left) - getDepth(root.right) ) <= 1 and \
                       self.isBalanced(root.left) and self.isBalanced(root.right) \
                       else False
        """
        # TODO: Bottom-Up recursion : fast
        def getHeight(root):
            if root is None: return 0
            leftHeight = getHeight(root.left)
            if leftHeight < 0: return -1
            rightHeight = getHeight(root.right)
            if rightHeight < 0: return -1
            return -1 if ( abs(leftHeight - rightHeight) > 1 ) else max(leftHeight, rightHeight) + 1
        
        return getHeight(root) >= 0

        
