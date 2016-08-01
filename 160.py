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
        dict_table = {}
        node = headA
        while node != None:
            dict_table[node] = node.val
            node = node.next
        node2 = headB
        while node2 != None:
            if node2 in dict_table.keys():
                return node2
            node2 = node2.next
        return None
