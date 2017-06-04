class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numStack, mainStack, bakStack, n = [], [], [], 0
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                numStack.append(n)
                bakStack.append(mainStack) # ...a2[b], push a to bak stack
                mainStack, n = [], 0 # for incoming b, meanwhile, bak stack stores [a]
            elif c == ']':
                bakStack[-1].extend(mainStack * numStack.pop() )# ...a2[b], get bb and extend to abb in bakStack
                mainStack = bakStack.pop() # mainStack = [abb] and bakStack = []
            else:
                mainStack.append(c)
        return "".join(mainStack)
