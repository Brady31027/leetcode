class Solution(object):
    def guessNumber(self, n):
        local_min, local_max = 1, n
        guess_num = int((local_min + local_max)/2)
        ret = guess(guess_num)
        while ret != 0:
            if ret == 1: # guess is lower
                local_min = guess_num
            elif ret == -1: # guess is higher
                local_max = guess_num
            guess_num = int((local_min + local_max)/2)
            ret = guess(guess_num)
        return guess_num
