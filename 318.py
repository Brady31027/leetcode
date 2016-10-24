class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_prod, dict_nums = 0, {}
        for w in words:
            w_sum = 0
            for c in set(w): w_sum |= 1 << (ord(c) - 97)
            dict_nums[w_sum] = max(dict_nums.get(w_sum, 0), len(w))
        for x in dict_nums:
            for y in dict_nums:
                if not x & y:
                    prod = dict_nums[x] * dict_nums[y]
                    if prod > max_prod: max_prod = prod
        return max_prod
