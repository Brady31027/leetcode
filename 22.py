class Solution(object):
    #http://stackoverflow.com/questions/23413881/understanding-function-to-generate-parentheses
    l_result = []
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return self.l_result
        self.l_result = []
        def recursion(n, s):
            if len(s) < n * 2:
                left, right = s.count('('), s.count(')')
                if left == right: recursion(n, s+'(')
                else:
                    if left < n: recursion(n, s+'(')
                    recursion(n,s+')')
            else:
                self.l_result.append(s)
                return
        
        recursion(n, "")
        return self.l_result
    
        
