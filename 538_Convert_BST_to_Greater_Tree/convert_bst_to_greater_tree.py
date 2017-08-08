# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        def dfs(node):
            if node:
                dfs(node.right)
                node.val += self.total
                self.total = node.val
                dfs(node.left)
        
        dfs(root)
        return root
        
            
        
