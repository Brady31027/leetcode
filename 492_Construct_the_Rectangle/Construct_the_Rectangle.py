class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l_dim = [area, 1]
        tmp_l = int(math.ceil(math.sqrt(area)))
        while tmp_l > 1:
            if area % tmp_l == 0:
                tmp_w = area//tmp_l
                l_dim = [max(tmp_l, tmp_w), min(tmp_l, tmp_w)]
                break
            tmp_l -= 1
        return l_dim
