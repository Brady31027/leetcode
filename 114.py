# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(0)
        l_stack = [root]
        while l_stack:
            node = l_stack.pop()
            if not node: continue
            l_stack.append(node.right)
            l_stack.append(node.left)
            dummy.right = node
            dummy.left = None
            dummy = node
        
                
        
