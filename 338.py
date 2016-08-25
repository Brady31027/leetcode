class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l_ans = []
        for n in range(num+1):
            l_ans.append(bin(n).count('1'))
        return l_ans
        
