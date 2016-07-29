# Need perf tuning
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.paths = []
        if root == None:
            return self.paths
        def dfs(root, path):
            if root.left == None and root.right == None:
                self.paths.append(path)
            if root.left != None:
                dfs(root.left, path + '->' + str(root.left.val))
            if root.right != None:
                dfs(root.right, path + '->' + str(root.right.val))
        dfs(root, str(root.val))
        return self.paths
