class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        while ver1 or ver2:
            v1, v2 = 0, 0
            if ver1: 
                v1Str = ver1.pop(0).lstrip('0')
                if not v1Str: v1Str = '0'
                v1 = int(v1Str)
            if ver2:
                v2Str = ver2.pop(0).lstrip('0')
                if not v2Str: v2Str = '0'
                v2 = int(v2Str)
            if v1 > v2: return 1
            elif v1 < v2: return -1
        return 0
            
