tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum, ans):
            if not root: return
            if not root.left and not root.right:
                if root.val == sum:
                    ans += [root.val]
                    global_ans.append(ans)
                return
            dfs(root.left, sum - root.val, ans + [root.val])
            dfs(root.right, sum - root.val, ans + [root.val])
            
        if not root: return []
        global_ans, ans = [], []
        dfs(root, sum, ans)
        return global_ans
                    
