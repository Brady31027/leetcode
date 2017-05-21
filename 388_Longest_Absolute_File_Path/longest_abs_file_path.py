class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxLength = 0
        pathTbl = {0: 0} # {depth: length}
        for line in input.splitlines():
            base = line.lstrip('\t')
            depth = len(line) - len(base)
            if '.' in base: # file
                maxLength = max(maxLength, pathTbl[depth] + len(base))
            else:
                pathTbl[depth + 1] = pathTbl[depth] + len(base) + 1 # +1 is for / symbol
        return maxLength
