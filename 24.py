# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        #  P -> O -> 1 -> 2 -> 3
        dummy = t = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            t = p.next.next
            p.next.next = t.next
            t.next = p.next
            p.next = t
            p = p.next.next
        return dummy.next
