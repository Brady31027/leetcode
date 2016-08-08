class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        common, common_tmp = strs[0], ""
        compare_len = 0
        for i in range(1, len(strs)):
            in_str = strs[i]
            compare_len = min( len(common), len(in_str))
            for i_c in range(compare_len):
                if common[i_c] != in_str[i_c]: break
                else: common_tmp += common[i_c]
            common = common_tmp
            common_tmp = ""
            if len(common) == 0: return ""
        return common        
            
