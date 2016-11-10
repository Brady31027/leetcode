class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        size1, size2 = len(s1), len(s2)
        if size1 + size2 != len(s3):return False
        ll_map = [[False for x in xrange(size1+1)] for y in xrange(size2+1)]
        ll_map[0][0] = True
        for x in xrange(1, size1+1): ll_map[0][x] = ll_map[0][x-1] and s1[x-1] == s3[x-1]
        for y in xrange(1, size2+1): ll_map[y][0] = ll_map[y-1][0] and s2[y-1] == s3[y-1]
        for y in xrange(1,size2+1):
            for x in xrange(1,size1+1):
                ll_map[y][x] = (ll_map[y][x-1] and s1[x-1] == s3[y+x-1]) or (ll_map[y-1][x] and s2[y-1] == s3[y+x-1])
        return ll_map[size2][size1]
        
