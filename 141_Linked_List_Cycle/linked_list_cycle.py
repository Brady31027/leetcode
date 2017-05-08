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
        while slowPtr and fastPtr:
            if not fastPtr.next or not fastPtr.next.next: return False
            slowPtr, fastPtr = slowPtr.next, fastPtr.next.next
            if slowPtr.val == fastPtr.val: return True
        return False
        
