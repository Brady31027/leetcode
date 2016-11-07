# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        l_ans, l_stack =[], [root]
        while l_stack:
            for i in xrange(len(l_stack)):
                node = l_stack.pop(0)
                if i == 0: l_ans.append(node.val)
                if node.right: l_stack.append(node.right)
                if node.left: l_stack.append(node.left)
        return l_ans
