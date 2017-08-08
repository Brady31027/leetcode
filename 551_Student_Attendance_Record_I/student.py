class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = collections.Counter(re.findall('LLL|A', s))
        if count['A'] > 1 or count['LLL'] > 0: return False 
        return True
