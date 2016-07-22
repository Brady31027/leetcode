class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        0	0
	1	1
	2	2
	3	3
	4	4
	5	5
	6	6
	7	7
	8	8
	9	9
	10	1
	11	2
	12	3
        """
        return num if num < 10 else (num - 1 ) % 9 + 1
