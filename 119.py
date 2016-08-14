class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Hint: Any row can be constructed using the offset sum of the previous row
        row = [1]
        for i in range(rowIndex):
            row = [u + v for u, v in zip(row+[0], [0]+row)]
        return row
