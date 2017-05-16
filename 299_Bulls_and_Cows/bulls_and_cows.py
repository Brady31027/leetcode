class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        B = sum((collections.Counter(guess) & collections.Counter(secret)).values())
        A = sum(itertools.imap( operator.eq, secret, guess))
        return "%dA%dB"%(A, B-A)
        
        # another solution -> faster !
        # A, B = sum(map(lambda x, y: x == y, secret, guess)), sum( min(secret.count(x), guess.count(x)) for x in "0123456789")
