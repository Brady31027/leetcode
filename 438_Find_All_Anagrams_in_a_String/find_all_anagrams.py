class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        patternHash = collections.Counter(p)
        count, patternLength, start, end, ans = len(p), len(p), 0, 0, []
        for i in range(len(s)):
            if patternHash[s[i]] > 0:
                count -= 1
            incomingChar = s[i]
            patternHash[incomingChar], end = patternHash[incomingChar] - 1, end + 1
            
            if count == 0:
                ans.append(start)
            
            if end - start >= patternLength:
                if patternHash[s[start]] >= 0:
                    count += 1
                fadeOutChar = s[start]
                patternHash[fadeOutChar], start =  patternHash[fadeOutChar] + 1, start + 1
        return ans
