# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        ans, queue, queue2 = [root.val], [root], []
        cnt, total = 0, 0
        while queue:
            for node in queue:
                if node.left: 
                    queue2.append(node.left)
                    cnt += 1
                    total += node.left.val
                if node.right: 
                    queue2.append(node.right)
                    cnt += 1
                    total += node.right.val
            if cnt > 0: ans.append(float(total)/cnt)
            queue, queue2 = queue2, []
            cnt, total = 0, 0
        return ans
        
