class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if re.search("^[A-Z]*$", word): return True
        elif re.search("^[A-Z]{0,1}[^A-Z]*$", word): return True
        return False
