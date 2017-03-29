# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue1, queue2, queue_in_view = [root], [], [root.val]
        while queue1:
            for node in queue1:
                if node.left: queue2.append(node.left)
                if node.right: queue2.append(node.right)
            if queue2: queue_in_view.append(queue2[-1].val)
            queue1,queue2 = queue2, []
        return queue_in_view
