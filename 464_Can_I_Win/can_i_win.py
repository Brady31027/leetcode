class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def win(choosable_mask, desired_total, current_sum, memo):
            if not choosable_mask: return False
            mask_key = tuple(choosable_mask)
            ans = memo.get(mask_key)
            if ans != None: # cache hit
                return memo[mask_key]
            else: # cache missed
                memo[mask_key] = False
                if choosable_mask[-1] + current_sum >= desired_total:
                    memo[mask_key] = True
                else:    
                    for i, choose in enumerate(choosable_mask):
                        if not win(choosable_mask[:i] + choosable_mask[i+1:], desired_total, current_sum + choose, memo):
                            memo[mask_key] = True
                            break
            return memo[mask_key]
            
        mask = [x for x in range(1, maxChoosableInteger + 1)]
        if sum(mask) < desiredTotal: return False
        return win(mask, desiredTotal, 0, {})
