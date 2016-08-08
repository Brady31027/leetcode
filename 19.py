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
        
        list_len = 0
        cur = head
        while cur is not None:
            list_len += 1
            cur = cur.next
        cut_idx = 0
        cut_target = list_len - n - 1
        
        if cut_target < 0: 
            head = head.next
            return head
        
        cur = head
        while cur is not None:
            if cut_idx == cut_target:
                cur.next = cur.next.next
            cut_idx += 1
            cur = cur.next
        return head
