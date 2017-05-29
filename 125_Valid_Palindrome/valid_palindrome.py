class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        head, tail = 0, len(s) - 1
        while head < tail:
            if s[head] != s[tail]:
                return False
            head, tail = head + 1, tail - 1
        return True
        
