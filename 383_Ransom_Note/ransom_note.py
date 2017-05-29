class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazineTbl = collections.Counter(magazine)
        for c in ransomNote:
            if c not in magazineTbl: return False
            else:
                if magazineTbl[c] == 0: return False
                magazineTbl[c] -= 1
        return True
