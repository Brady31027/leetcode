# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1) == True:
            return 1
        else:
            latest_good, first_bad, test = 1, n, int(n/2)
            while first_bad - latest_good > 1:
                if isBadVersion(test) == True:
                    first_bad = test
                else:
                    latest_good = test
                test = int( latest_good + (first_bad - latest_good)/2 )
            return first_bad
