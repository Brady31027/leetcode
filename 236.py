# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        l_ans = []
        
        def check(root, p, q):
            if not root: return False
            l_path, l_stack = [], [root]
            while l_stack:
                node = l_stack.pop()
                if node.left: 
                    l_stack.append(node.left)
                    l_path.append(node.left)
                if node.right: 
                    l_stack.append(node.right)
                    l_path.append(node.right)
            if p in l_path and q in l_path: return True
            else: return False
                
            
        def postOrderTraversal(root, l_ans):
            if not root: return
            postOrderTraversal(root.left, l_ans)
            postOrderTraversal(root.right, l_ans)
            l_ans.append(root)
            
        postOrderTraversal(root, l_ans)
        for node in l_ans:
            result = check(node, p, q)
            if result == True: return node
        return root
