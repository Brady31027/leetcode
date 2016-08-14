class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        #str_sorted = sorted(strs) # from sm to bi
        strs.sort() # inplace sorting is faster
        str_a, str_b = strs[0], strs[-1]
        common = ""
        for idx_c in range(len(str_a)):
            if str_a[idx_c] != str_b[idx_c]: break
            common += str_a[idx_c]
        return common
            
