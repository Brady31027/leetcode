class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tbl, stack = {')':'(', ']': '[', '}': '{' }, []
        for c in s:
            if c in [ '(', '[', '{' ]:
                stack.append(c)
            else:
                if not stack or stack.pop() != tbl.get( c ):
                    return False
        return True if not stack else False
