ass Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Hint: Any row can be constructed using the offset sum of the previous row
        # Detail: https://discuss.leetcode.com/topic/22628/python-4-lines-short-solution-using-map
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
