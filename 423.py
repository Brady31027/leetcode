class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_ans, l_statistics = "", [0] * 10
        for c in s:
            if c == 'z': l_statistics[0] += 1
            elif c == 'w': l_statistics[2] += 1
            elif c == 'u': l_statistics[4] += 1
            elif c == 'x': l_statistics[6] += 1
            elif c == 'g': l_statistics[8] += 1
            elif c == 'h': l_statistics[3] += 1
            elif c == 'f': l_statistics[5] += 1
            elif c == 'v': l_statistics[7] += 1
            elif c == 'o': l_statistics[1] += 1
            elif c == 'i': l_statistics[9] += 1
        l_statistics[3] -= l_statistics[8]
        l_statistics[5] -= l_statistics[4]
        l_statistics[7] -= l_statistics[5]
        l_statistics[1] -= (l_statistics[0] + l_statistics[2] + l_statistics[4])
        l_statistics[9] -= (l_statistics[5] + l_statistics[6] + l_statistics[8])
        for i in xrange(10):
            if l_statistics[i] > 0:
                str_ans += str(i)*l_statistics[i]
        return str_ans
        
