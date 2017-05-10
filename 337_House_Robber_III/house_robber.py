# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        def dfs(root):
            if not root: return [0, 0]
            leftCandidates = dfs(root.left)
            rightCandidates = dfs(root.right)
            withPick = root.val + leftCandidates[1] + rightCandidates[1] 
            withoutPick = max(leftCandidates[0], leftCandidates[1]) + max(rightCandidates[0], rightCandidates[1])
            return [withPick, withoutPick]
        
        candidates = dfs(root)
        return max(candidates[0], candidates[1])
        
        
