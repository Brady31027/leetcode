# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = cursor = ListNode(0)
        cur = head
        while cur:
            if cur.val == val:
                cursor.next = cur.next
            else:
                cursor.next = cur
                cursor = cur
            cur = cur.next
        return dummy.next
