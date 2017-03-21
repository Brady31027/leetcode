# Definition for a binary tree node.
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
        if not root: return []
        queue1, queue2 = [root], []
        ans, local_ans = [], []
        while len(queue1):
            for node in queue1:
                local_ans.append(node.val)
                if node.left: queue2.append(node.left)
                if node.right: queue2.append(node.right)
            queue1, queue2 = queue2, []
            ans = [local_ans] + ans
            local_ans = []
        return ans
