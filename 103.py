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
        ll_ans, l_stack, cnt = [[root.val]], [root], 0
        while l_stack:
            l_stack2, l_ans = [], []
            size = len(l_stack)
            for i in xrange(size):
                node = l_stack.pop(0)
                if node.left:
                    l_ans.append(node.left.val)
                    l_stack2.append(node.left)
                if node.right:
                    l_ans.append(node.right.val)
                    l_stack2.append(node.right)
            l_stack = l_stack2
            if cnt % 2 == 0: l_ans = list(reversed(l_ans))
            cnt += 1
            if len(l_ans): ll_ans.append(l_ans)
        return ll_ans
            
        
