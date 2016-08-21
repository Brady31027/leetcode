
from itertools import permutations

class Solution(object):
    
    def find_all(self, s, pattern, l_result):
        start = 0
        while True:
            start = s.find(pattern, start)
            if start == -1: return
            if start not in l_result: l_result.append(start)
            start += 1
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l_result, l_pattern = [], []
        for m in permutations(words):l_pattern.append("".join(m))
        for pattern in l_pattern: self.find_all(s, pattern, l_result)
        return l_result
