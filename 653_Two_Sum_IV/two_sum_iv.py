# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        queue, tbl = [root], set()
        while queue:
            node = queue.pop(0)
            if k - node.val in tbl:
                return True
            tbl.add(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False
