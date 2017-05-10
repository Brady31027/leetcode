# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = cursor = ListNode(0)
        cur = head
        setBook = set()
        while cur:
            if cur.val not in setBook and cur.next and cur.val != cur.next.val:
                cursor.next = cur
                setBook.add(cur.val)
                cursor = cur
            elif not cur.next: # last node
                if cur.val not in setBook:
                    cursor.next = cur
                else: cursor.next = None
            else: # redundant node
                cursor.next = cur.next
                setBook.add(cur.val)
            cur = cur.next
        return dummy.next
