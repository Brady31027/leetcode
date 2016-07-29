# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        prerequisite: understand what BST is!
        p, q are on left, then lca is on left
        p, q are on right, then lca is on right
        p, q are on left and right seperately, then lca is the root
        """
        if root == None:
            return root
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val and q.val >= root.val:
            return root
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
            
            
