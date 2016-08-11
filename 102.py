# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BSF, swap queue
        if root is None: return []
        l_result, l_visit = [], [root]
        while len(l_visit):
            l_tmp, l_visit2 = [], []
            # avoit 2 pass solution
            #l_result.append([node.val for node in l_visit])
            for node in l_visit:
                l_tmp.append(node.val)
                if node.left: l_visit2.append(node.left)
                if node.right: l_visit2.append(node.right)
            l_result.append(l_tmp)
            l_visit = l_visit2
        return l_result
        