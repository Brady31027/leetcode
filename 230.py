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
        cnt, node, l_stack = 0, root, []
        while node:
            l_stack.append(node)
            node = node.left
        while l_stack and cnt < k:
            node = l_stack.pop() # min
            cnt += 1
            right = node.right
            while right:
                l_stack.append(right)
                right = right.left
        return node.val
        
