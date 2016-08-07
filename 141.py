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
        fast = slow = head
        if fast is None or fast.next is None:
            return False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        '''
        set_node = set()
        if head is None:
            return False
        while head != None:
            if head in set_node:
                return True
            set_node.add(head)
            head = head.next
        return False
        '''
