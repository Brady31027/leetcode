# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # TODO: Learn Morris Traversal
        if not root: return []
        
        count = collections.Counter()
        
        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        mode = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == mode]
        
        
