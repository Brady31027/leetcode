# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def convert(l_n):
            size = len(l_n)
            if size == 0: return None
            elif size == 1: return TreeNode(l_n[0])
            root = TreeNode(l_n[size//2])
            root.left = convert(l_n[:size//2])
            root.right = convert(l_n[size//2+1:])
            return root
            
        if not head: return None
        l_nums = []
        while head is not None and head.val is not None: 
            l_nums.append(head.val)
            head = head.next
        root = convert(l_nums)
        return root
        
