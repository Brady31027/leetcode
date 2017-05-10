# Definition for singly-linked list.
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
        carry = 0
        cursor = head = ListNode(0)
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            current = (total + carry) % 10
            carry = (total + carry) / 10
            # add node to the tail
            node = ListNode(current)
            cursor.next = node
            cursor = node
        # handle overflow carry digit    
        if carry > 0:
            node = ListNode(carry)
            cursor.next = node
        return head.next
