class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tokens = path.split('/')
        for token in tokens:
            if not token or token == '.': continue
            elif token == '..': 
                if not stack: continue
                stack.pop()
            else: stack.append(token)
        return '/'+'/'.join(stack)
        
