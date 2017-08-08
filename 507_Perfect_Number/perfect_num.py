class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return False
        head, total = 2, 1
        while head * head <= num:
            if num % head == 0:
                tail = num / head    
                if head != tail: total += head + tail
                else: total += head
                if total > num: return False
            head += 1
        return total == num
        
