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
        if not head or not head.next or k == 0: return head
        size, cursor = 1, head
        
        # calculate size
        while cursor and cursor.next:
            cursor = cursor.next
            size += 1
        k %= size
        if k == 0: return head # complete circle, early reject
        
        cursor.next = head
        tail, cursor = cursor, head # round back to head
        
        # find the tailing node and break its next relation
        for _ in xrange(size - k):
            tail = cursor
            cursor = cursor.next
        tail.next = None
        return cursor
            
        
