# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        l_node = []
        node = head
        while node != None:
            l_node.append(node.val)
            node = node.next
        l_reverse_node = l_node[::-1]
        return False if l_node != l_reverse_node else True
