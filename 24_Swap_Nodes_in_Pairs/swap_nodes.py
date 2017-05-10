# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cursor = dummy
        while cursor.next and cursor.next.next:
            nextOne, nextTwo, nextThree = cursor.next, cursor.next.next, cursor.next.next.next
            cursor.next = nextTwo
            nextOne.next = nextThree
            nextTwo.next = nextOne
            cursor = nextOne
        return dummy.next
