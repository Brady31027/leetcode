class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        boomerangs = 0
        for index1, [x1, y1] in enumerate(points):
            disTable = collections.defaultdict(int)
            for index2, [x2, y2] in enumerate(points):
                if index1 == index2: continue
                disTable[ (x1 - x2) ** 2 + (y1 - y2) ** 2 ] += 1
            for key, value in disTable.iteritems():
                if value > 1:
                    boomerangs += ( value * (value - 1) )
        return boomerangs
