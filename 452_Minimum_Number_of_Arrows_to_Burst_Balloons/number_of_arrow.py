class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        size = len(points)
        if size < 2: return 0 if size == 0 else 1
        arrow_cnt = 1
        points.sort(key=lambda x: x[0])
        for i in range(1, size):
            if points[i][0] <= points[i-1][1]:
                points[i][1] = min(points[i][1], points[i-1][1])
            else:
                arrow_cnt += 1
        return arrow_cnt
