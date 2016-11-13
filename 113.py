# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ll_ans = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        l_path, self.ll_ans = [], []
         
        def dfs(root, l_path, total):
            if not root: return
            if root.left is None and root.right is None and total - root.val == 0:
                self.ll_ans.append(l_path)
                return
            total = total - root.val
            if root.left: dfs(root.left, l_path + [root.left.val], total)
            if root.right: dfs(root.right, l_path + [root.right.val], total)
        
        dfs(root, l_path + [root.val], sum)
        return self.ll_ans
