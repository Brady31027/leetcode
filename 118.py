class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ll_result, l_row = [], []
        for i in range( numRows):
            # expand more, performance boosts more
            if i == 0:
                l_row = [1]
            elif i == 1:
                l_row = [1, 1]
            elif i == 2:
                l_row = [1, 2, 1]
            elif i == 3:
                l_row = [1, 3, 3, 1]
            else:
                l_row = [0] * (i+1) # 0 base or 1 base
                for j in range(i+1):
                    if j == 0 or j == i: # i and j are both 1 base
                        l_row[j] = 1
                    else:
                        l_row[j] = ll_result[-1][j-1] + ll_result[-1][j]
            ll_result.append(l_row)
        return ll_result
