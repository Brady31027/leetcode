# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack, rank = [], 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                rank += 1
                element = stack.pop()
                if rank == k: return element.val
                root = element.right
        return 0 # should not come here
