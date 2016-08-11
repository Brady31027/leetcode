class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(s):
            length, cnt, result = len(s), 1, ""
            for i, c in enumerate(s):
                if i+1 < length and s[i] != s[i+1]:
                    result += str(cnt) + c
                    cnt = 1
                elif i+1 < length:
                    cnt += 1
            result += str(cnt) + c
            return result
            
            
        result = '1'
        for i in range(1, n):
            result = say(result)
        return result    
        
