class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l_v1 = version1.split('.')
        l_v2 = version2.split('.')
        len_diff = len(l_v1) - len(l_v2)
        if len_diff < 0: # v1 is shorter
            for i in xrange(-len_diff):
                l_v1.append('0')
        elif len_diff > 0: # v2 is shorter
            for i in xrange(len_diff):
                l_v2.append('0')
        for i in xrange(len(l_v1)):
            if int(l_v1[i]) < int(l_v2[i]):
                return -1
            elif int(l_v1[i]) > int(l_v2[i]):
                return 1
        return 0
