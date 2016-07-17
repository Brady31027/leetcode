# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        n_div_by_2 = int(n/2) #force to trancate
        ret = guess(n_div_by_2)
        while ret != 0:
            if ret == -1: # guess is lower
                n_div_by_2 = int((n + n_div_by_2) / 2)
            elif ret == 1: # guess is higher
                n_div_by_2 = int(n_div_by_2/2)
            ret = guess(n_div_by_2)
        return n_div_by_2;
