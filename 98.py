# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l_ans, l_stack = [], []
        while root or l_stack:
            if root:
                l_stack.append(root)
                root = root.left
            else:
                root = l_stack.pop()
                l_ans.append(root.val)
                root = root.right
        for i in xrange(1, len(l_ans)):
            if l_ans[i] <= l_ans[i-1]: return False
        return True
            
