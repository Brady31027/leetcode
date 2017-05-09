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
        setBook = set()
        prev, cur = ListNode(0), head
        while cur:
            if cur.val in setBook:
                prev.next = cur.next
            else:
                prev = cur
                setBook.add(cur.val)
            cur = cur.next
        return head
