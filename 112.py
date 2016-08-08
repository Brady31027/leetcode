# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    total = 0
    result = False
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #total = 0
        set_visited = set()
        
        if root is None:
            return False
        
        # dfs is better
        def dfs(node):
            if self.result == True: return
            self.total += node.val
            if node.left and node.left not in set_visited:
                set_visited.add(node.left)
                dfs(node.left)
            if node.right and node.right not in set_visited:
                set_visited.add(node.right)
                dfs(node.right)
            if node.left is None and node.right is None:
                #print self.total
                if self.total == sum: self.result = True
                else: self.total -= node.val
            else:
                self.total -= node.val
                return
        dfs(root)
        return self.result
        
