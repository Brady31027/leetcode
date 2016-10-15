class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        collection_ransom = collections.Counter(ransomNote)
        collection_magazine = collections.Counter(magazine)
        set_ransom = set(ransomNote)
        set_magazine = set(magazine)
        for c in set_ransom:
            if c not in set_magazine: return False
            elif collection_ransom[c] > collection_magazine[c]: return False
        return True
        
