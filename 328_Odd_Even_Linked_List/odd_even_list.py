# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        oddCursor = oddHead = head
        evenCursor = evenHead = head.next
        
        while evenCursor and evenCursor.next:
            oddCursor.next = evenCursor.next
            oddCursor = oddCursor.next
            evenCursor.next = oddCursor.next
            evenCursor = evenCursor.next
        oddCursor.next = evenHead
       
        return oddHead
