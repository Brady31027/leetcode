tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # BFS; swap queue
        if root is None: return True
        l_visit = [root]
        while l_visit:
            l_children = []
            for n in l_visit: l_children.extend([n.left, n.right])
            l_children_val = [ (node.val if node else None) for node in l_children]
            if l_children_val != l_children_val[::-1]: return False
            l_visit = [node for node in l_children if node]
        return True
