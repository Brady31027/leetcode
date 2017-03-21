# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        left_to_right = True
        queue1, queue2 = [root], []
        ans, local_ans = [], []
        while len(queue1):
            for node in queue1:
                local_ans = local_ans + [node.val] if left_to_right else [node.val] + local_ans
                if node.left: queue2.append(node.left)
                if node.right: queue2.append(node.right)
            queue1, queue2 = queue2, []
            left_to_right = not left_to_right
            ans.append(local_ans)
            local_ans = []
        return ans
                
