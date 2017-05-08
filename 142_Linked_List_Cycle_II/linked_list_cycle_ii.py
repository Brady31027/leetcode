# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr, fastPtr = slowPtr.next, fastPtr.next.next
            if fastPtr is slowPtr:
                fastPtr = head
                while fastPtr is not slowPtr:
                    fastPtr, slowPtr = fastPtr.next, slowPtr.next
                return fastPtr
        return None
        
        
