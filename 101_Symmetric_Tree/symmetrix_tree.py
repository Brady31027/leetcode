# Definition for a binary tree node.
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
        if not root: return True
        stack = [root.left, root.right]
        while stack:
            l, r = stack.pop(), stack.pop()
            if not l and not r: continue
            if not l or not r or l.val != r.val: return False
            stack.append(l.left)
            stack.append(r.right)
            stack.append(l.right)
            stack.append(r.left)
        return True
        """
        #[recursive] 
        if root is None: return True
        def isMirror(l, r):
            if l is None and r is None: return True
            elif (l is None) ^ (r is None): return False
            else: return (l.val == r.val) and isMirror(l.left, r.right) and isMirror(l.right, r.left)
        
        return isMirror(root.left, root.right)
        """
