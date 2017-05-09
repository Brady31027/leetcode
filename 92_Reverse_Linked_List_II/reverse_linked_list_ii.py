# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = head
        offset = dummy
        
        # find offset
        for _ in xrange(m - 1):
            offset.next = cur
            offset = offset.next
            cur = cur.next
        
        # reverse selected range
        end, tmp, start = None, None, cur
        for _ in xrange(m, n + 1):
            tmp = start.next
            start.next = end # init to None
            end = start      # final value is 4 subject to [1,2,3,4,5] with param (2, 4)
            start = tmp      # final value is 5 subject to [1,2,3,4,5] with param (2, 4)
        
        # combine range
        offset.next = end # 1 -> 4 -> 3 -> 2,  5
        cur.next = start  # 1 -> 4 -> 3 -> 2 -> 5
        
        return dummy.next
