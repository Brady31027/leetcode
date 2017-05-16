# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
    
        firstHalfHead, firstHalfTail, secondHalfHead = head, head, None
        slow = fast = ListNode(0)
        slow.next = head
        # for odd number of nodes, eg. 1 2 3 4 5, slow points to 3
        # for even number of nodes, eg. 1 2 3 4, slow points to 3
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        firstHalfTail = slow
        slow = slow.next
        firstHalfTail.next = None
        
        # reverse the second half
        while slow:
            tmp = slow.next
            slow.next = secondHalfHead
            secondHalfHead = slow
            slow = tmp

        # concate the first half and the second half
        cursor = ListNode(0)
        while firstHalfHead or secondHalfHead:
            if firstHalfHead:
                cursor.next = firstHalfHead
                firstHalfHead = firstHalfHead.next
                cursor = cursor.next
            if secondHalfHead:
                cursor.next = secondHalfHead
                secondHalfHead = secondHalfHead.next
                cursor = cursor.next
                
