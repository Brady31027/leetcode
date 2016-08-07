# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        set_node = set()
        if head is None:
            return False
        while head != None:
            if head in set_node:
                return True
            set_node.add(head)
            head = head.next
        return False
