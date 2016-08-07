class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dict_row = {0: [1],
                    1: [1, 1],
                    2: [1, 2, 1],
                    3: [1, 3, 3, 1]}
                    
        #expand more, performance boosts more
        if rowIndex < 4:
            return dict_row[rowIndex]
        else:
            l_prev_row, l_row = dict_row[3], [0]*(rowIndex + 1)
            for i in range(4, rowIndex + 1, 1):
                midIndex = i/2 # 0 base to 1 base 
                for j in range(0, midIndex + 1 , 1):
                    if j == 0:
                        l_row[j] = l_row[i - j] = 1
                    else:
                        l_row[j] = l_row[i - j] = l_prev_row[j-1] + l_prev_row[j]
                l_prev_row = list(l_row)
            return l_row
