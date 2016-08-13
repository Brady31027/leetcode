class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        elif p and q and p.val == q.val: return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        else: return False
