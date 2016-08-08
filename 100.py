# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        l_tree1, l_tree2 = [], []
        if p is not None: l_tree1.append(p)
        if q is not None: l_tree2.append(q)
        if len(l_tree1) != len(l_tree2): return False
        while len(l_tree1):
            p = l_tree1.pop(0)
            q = l_tree2.pop(0)
            if p.val != q.val: return False
            if p.left: l_tree1.append(p.left)
            if q.left: l_tree2.append(q.left)
            if len(l_tree1) != len(l_tree2): return False
            if p.right: l_tree1.append(p.right)
            if q.right: l_tree2.append(q.right)
            if len(l_tree1) != len(l_tree2): return False
        return True
