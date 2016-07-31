class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # do we need to handle flip?
        # first rectangle
        a = (C-A) * (D-B)
        # second rectangle
        b = (G-E) * (H-F)
        # overlap area
        c = 0
        if C <= E or A >= G or B >= H or F >= D:
            c = 0
        else:
            max_x1 = max(A, E)
            max_y1 = max(B, F)
            min_x2 = min(C, G)
            min_y2 = min(D, H)
            c = (min_x2 - max_x1) * (min_y2 - max_y1)
        return a + b - c
