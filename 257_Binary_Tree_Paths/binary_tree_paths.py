# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        global_path = []
        def dfs(root, local_path):
            if not root: return
            if root.left:
                dfs(root.left, local_path + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, local_path + '->' + str(root.right.val))
            if not root.left and not root.right:
                global_path.append(local_path)
        
        if not root: return []
        dfs(root, str(root.val))
        return global_path
            
            
        
