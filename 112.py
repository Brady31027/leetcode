# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
      def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: return False
        if not root.left and not root.right: return sum == root.val
        #if root.left:
        #    left = self.hasPathSum(root.left, sum - root.val)
        #    if left: return True
        #if root.right:
        #    right = self.hasPathSum(root.right, sum - root.val)
        #    if right: return True
        #return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
