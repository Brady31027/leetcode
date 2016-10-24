class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_prod, long_w, short_w = 0,"",""
        for w1 in words:
            for w2 in words:
                if len(w1) >= len(w2): long_w, short_w = w1, w2
                if len(list(set(long_w) - set(short_w))) < len(set(long_w)): continue
                else:
                    prod = len(long_w) * len(short_w)
                    if prod > max_prod:
                        max_prod = prod
        return max_prod
        
