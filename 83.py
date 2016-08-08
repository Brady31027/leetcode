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
        set_book = set()
        cur = head
        prev = ListNode(0)
        while cur is not None:
            if cur.val in set_book:
                prev.next = cur.next
            else:
                set_book.add(cur.val)
                prev = cur
            cur = cur.next
        return head
