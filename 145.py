# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        l_ans = []
        
        def traversal(root, l_ans):
            if not root: return
            traversal(root.left, l_ans)
            traversal(root.right, l_ans)
            l_ans.append(root.val)
            return l_ans
        
        traversal(root, l_ans)
        return l_ans
