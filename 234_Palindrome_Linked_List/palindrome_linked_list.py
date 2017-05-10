# Definition for singly-linked list.
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
        if not head: return True
        
        # find mid point and seperate list to two parts
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        
        # reverse the second part
        secondPartCursor, secondPartPrev = mid, None
        while secondPartCursor:
            tmp = secondPartCursor.next
            secondPartCursor.next = secondPartPrev
            secondPartPrev = secondPartCursor
            secondPartCursor = tmp
        
        # identify whether the first part is the same as the second part
        firstPartCursor = head
        while secondPartPrev:
            if firstPartCursor.val != secondPartPrev.val:
                return False
            firstPartCursor = firstPartCursor.next
            secondPartPrev = secondPartPrev.next
        return True
        
