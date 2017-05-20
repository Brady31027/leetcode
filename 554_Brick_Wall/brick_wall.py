class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        boundary = collections.Counter()
        for row in xrange(len(wall)):
            accumulatedWidth = 0
            for col in xrange(len(wall[row]) - 1):
                accumulatedWidth += wall[row][col]
                boundary[accumulatedWidth] += 1
        verticalLineCandidates = filter( lambda (k, v): k > 0 , [ (k, v) for k, v in boundary.iteritems()] )
        verticalLineRepeatCount = 0
        if len(verticalLineCandidates) > 0:
            verticalLineRepeatCount = max(verticalLineCandidates, key=lambda tup: tup[1])[1]
        return len(wall) - verticalLineRepeatCount
