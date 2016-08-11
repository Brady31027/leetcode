# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        
        head = cur = ListNode(0)
        is_head_set = False
        
        while l1 or l2:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                if is_head_set == False: head.next = cur.next 
                is_head_set = True
            elif l1 is not None:
                cur.next = l1
                l1 = l1.next
            elif l2 is not None:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return head.next