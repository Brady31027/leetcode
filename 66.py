class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num, l_result, size = '', [], len(digits)
        for i in digits: num += str(i) 
        for c in str(int(num) + 1): l_result.append(int(c))
        if len(l_result) < size: l_result.insert(0, 0)
        return l_result
