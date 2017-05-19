class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        maxLength, queue = 0, []
        for char in s:
            if char not in queue:
                queue.append(char)
            else:
                queue.pop(0)
                while char in queue:
                    queue.pop(0)
                queue.append(char)
            maxLength = max(maxLength, len(queue))
        return maxLength
            
                    
