# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        abs_value = []
        def dfs(node):
            if not node: return
            abs_value.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        abs_value.sort()
        min_dis = float("Inf")
        for i in range(1, len(abs_value)):
            min_dis = min(min_dis, abs_value[i] - abs_value[i-1])
        return min_dis
        
