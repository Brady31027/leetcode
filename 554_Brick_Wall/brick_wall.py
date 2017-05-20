class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        boundary = collections.Counter()
        for row in xrange(len(wall)):
            accumulatedWidth = 0
            for brick in wall[row]:
                if accumulatedWidth > 0: boundary[accumulatedWidth] += 1
                accumulatedWidth += brick # skip the last brick
        return len(wall) - (max(boundary.values() or [0]))
