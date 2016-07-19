class sol(object):
    def guess(self, target, guess):
        l_target = list(target) 
        l_guess = list(guess)
        target_book = 0x0000
        guess_book = 0x0000
        A, B = 0, 0
        # calculate As
        for idx in xrange(len(l_guess)):
            if l_target[idx] == l_guess[idx]:
                A += 1
                target_book |= (1 << idx)
                guess_book |= (1 << idx)
        for idx in xrange(len(l_guess)):
            if guess_book & (1 << idx):
                continue
	    l_found_idx = [i for i, x in enumerate(l_target) if x == l_guess[idx]]
            if len(l_found_idx) > 0:
		for found_idx in l_found_idx:
	            if target_book & (1 << found_idx) == 0:
                        target_book |= (1 << found_idx)
                        B += 1
                        break
        return "%dA%dB" %(A, B)

sol_obj = sol()
print sol_obj.guess("11", "10")

#print [1,2,2,3,4].index(2)
