class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remember to remove the tailing spaces
        return len((re.sub(r'\s+$','',s)).split(' ')[-1]) if s else 0
