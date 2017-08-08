class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        head, tail = 2, int(num/2 + 0.5)
        total = 1
        while head <= tail:
            if num % head == 0:
                tail = num // head
                
                if tail < head: break
                
                if head == tail: total += head
                else: total += head + tail
                
                if total > num: return False
            head += 1
        return True if total == num else False
            
        
        
