# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        dfs(root)
        return ans
