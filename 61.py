# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0: return head
        if not head: return []
        cursor, dup_head = head, ListNode(0)
        size = 1
        while cursor.next:
            size += 1
            cursor = cursor.next
        cursor.next = head
        shift = size - k % size
        while shift > 0:
            cursor = cursor.next
            shift -= 1
        dup_head = cursor.next
        cursor.next = None
        return dup_head
