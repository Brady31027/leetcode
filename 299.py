class sol(object):
    def guess(self, secret, guess):
        A, B = sum(map(lambda x, y: x == y, secret, guess)), sum( min(secret.count(x), guess.count(x)) for x in "0123456789") 
        B = B - A
        return "%dA%dB" %(A, B)

