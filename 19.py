# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0 or head is None: return head
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for i in range(n): first = first.next
        while first.next is not None:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next
