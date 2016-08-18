# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None: return None
        cur, head = ListNode(0), ListNode(0)
        head.next = cur
        carry = 0
        while l1 and l2:
            carry, cur.val = divmod(l1.val + l2.val + carry, 10)
            if l1.next or l2.next or carry != 0: cur.next = ListNode(0)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        while l1:
            carry, cur.val = divmod(l1.val + carry, 10)
            if l1.next or carry != 0: cur.next = ListNode(0)
            cur = cur.next
            l1 = l1.next
        while l2:
            carry, cur.val = divmod(l2.val + carry, 10)
            if l2.next or carry != 0: cur.next = ListNode(0)
            cur = cur.next
            l2 = l2.next
        if carry != 0: cur.val = carry
        return head.next
