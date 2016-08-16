class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val: cur.next = cur.next.next
            else: cur = cur.next
        return head
