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
        queue1, queue2 = [], []
        while l1:
            queue1.append(l1.val)
            l1 = l1.next
        while l2:
            queue2.append(l2.val)
            l2 = l2.next
        
        cursor = None # for output list
        carry = 0     # for calculation
        while queue1 or queue2:
            total = 0
            if queue1: total += queue1.pop()
            if queue2: total += queue2.pop()
            current = (carry + total) % 10
            carry = (carry + total)  / 10
            # add node to the front
            node = ListNode(current)
            node.next = cursor
            cursor = node
        # handle overflow
        if carry > 0:
            node = ListNode(carry)
            node.next = cursor
            cursor = node
        head = ListNode(0)
        head.next = cursor
        return head.next
            
