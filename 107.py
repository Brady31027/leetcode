# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        l_result, l_visit = [],[root]
        while l_visit:
            l_tmp,l_visit2 = [], []
            for node in l_visit:
                l_tmp.append(node.val)
                if node.left: l_visit2.append(node.left)
                if node.right: l_visit2.append(node.right)
            l_result.append(l_tmp)
            l_visit = l_visit2
        return l_result[::-1]  
        
