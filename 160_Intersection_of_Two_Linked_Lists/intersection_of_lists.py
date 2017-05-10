# Definition for singly-linked list.
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
        setBook = set()
        cursorA, cursorB = headA, headB
        while cursorA or cursorB:
            if cursorA:
                if cursorA not in setBook:
                    setBook.add(cursorA)
                    cursorA = cursorA.next
                else: return cursorA
            if cursorB:
                if cursorB not in setBook:
                    setBook.add(cursorB)
                    cursorB = cursorB.next
                else: return cursorB
        return None
        
