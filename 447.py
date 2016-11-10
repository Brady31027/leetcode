class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for n in points:
            dict_dis = {}
            for m in points:
                d = (n[0] - m[0])**2 + (n[1] - m[1])**2
                if d in dict_dis: dict_dis[d] += 1
                else: dict_dis[d] = 1
            for d in dict_dis:
                ans += (dict_dis[d] - 1) * dict_dis[d]
        return ans
