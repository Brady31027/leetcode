class Solution(object):
    
    def isValid(self, s):
        # can not handle other char or nested parentheses
        size = len(s)
        if size == 0: return True
        if size % 2 != 0: return False
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}','').replace('[]','').replace('()','')
        return len(s) == 0
        
        """
        # [following is the regular solution]
        dict_syntax = {'{':'}','[':']','(':')'}
        l_head = dict_syntax.keys()
        l_tail = dict_syntax.values()
   
   
        if len(s) == 0: return True
        if len(s) % 2 != 0: return False
        
        l_stack = []
        for c in s:
            if c in l_head: l_stack.append(c)
            elif c in l_tail:
                if len(l_stack) == 0: return False
                head = l_stack.pop()
                if c != dict_syntax[head]: return False
        if len(l_stack) > 0: return False
        return True
        """
