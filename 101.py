# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # BFS; swap queue
        if root is None: return True
        #if root.left is None and root.right is None: return True
        l_visit, l_children_idx = [root], []
        while l_visit:
            l_visit2, l_children_idx2 = [], []
            for idx in range(len(l_visit)):
                node = l_visit[idx]
                if node.left: 
                    l_visit2.append(node.left)
                    l_children_idx2.append(1)
                else:
                    l_children_idx2.append(0)
                if node.right: 
                    l_visit2.append(node.right)
                    l_children_idx2.append(1)
                else:
                    l_children_idx2.append(0)
                    
            l_visit = l_visit2
            l_children_idx = l_children_idx2
            
            if l_children_idx != l_children_idx[::-1]:
                return False
            
            if [n.val for n in l_visit] != [n.val for n in l_visit][::-1]: 
                return False
            
            
        return True
        
