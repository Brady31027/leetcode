class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if m == 0 and n == 0:
            return 0
        elif m == 0 and n != 0:
            return -1
        elif m != 0 and n == 0:
            return 0
        
        #KMP algorithm
        #step1. build shift table
        size = n
        pattern = list(needle)
        shift_table = [1] * (size + 1)
        shift = 1
        for pos in range(size):
            while shift <= pos and pattern[pos] != pattern[pos - shift]:
                shift += shift_table[pos - shift]
            shift_table[pos+1] = shift
        #step2. compare
        start_pos, match_len = 0, 0
        for c in haystack:
            while match_len == size or (match_len >= 0 and pattern[match_len] != c):
                start_pos += shift_table[match_len]
                match_len -= shift_table[match_len]
            match_len += 1
            if match_len == len(pattern):
                return start_pos
        return -1
