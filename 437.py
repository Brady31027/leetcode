# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, val):
            if not root: return 0
            ans = (val == root.val)
            ans += dfs(root.left, val - root.val)
            ans += dfs(root.right, val - root.val)
            return ans
        
        if not root: return 0
        ans = dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return ans
