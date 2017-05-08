# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr, fastPtr = slowPtr.next, fastPtr.next.next
            if slowPtr is fastPtr: return True
        return False
        
