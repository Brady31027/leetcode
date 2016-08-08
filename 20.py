class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        dict_syntax = {'{':'}','[':']','(':')'}
        l_head = dict_syntax.keys()
        l_tail = dict_syntax.values()
        l_stack = []
        for c in s:
            if c in l_head: l_stack.append(c)
            elif c in l_tail:
                if len(l_stack) == 0: return False
                head = l_stack.pop()
                if c != dict_syntax[head]: return False
        if len(l_stack) > 0: return False
        return True
