class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_prod, l_nums = 0, []
        for w in words:
            w_sum = 0
            for c in set(w): w_sum |= 1 << (ord(c) - ord('a'))
            l_nums.append(w_sum)
        size = len(words)    
        for w_i in xrange(size):
            for w_j in xrange(size):
                if l_nums[w_i] & l_nums[w_j] == 0: 
                    prod = len(words[w_j]) * len(words[w_i])
                    if prod > max_prod: max_prod = prod
        return max_prod
                
