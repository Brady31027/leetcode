# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallerList = smallerListHead = ListNode(0)
        largerList = largerListHead = ListNode(0)
        while head:
            if head.val < x:
                smallerList.next = head
                smallerList = smallerList.next
            else:
                largerList.next = head
                largerList = largerList.next
            head = head.next
        largerList.next = None
        smallerList.next = largerListHead.next
        return smallerListHead.next
        
