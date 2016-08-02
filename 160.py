# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        set_table = set()
        while headA:
            set_table.add(headA)
            headA = headA.next
        while headB:
            if headB in set_table:
                return headB
            headB = headB.next
        return None
