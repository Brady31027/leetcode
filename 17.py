mport itertools

class Solution(object):
    dict_keys = {
        '1':[],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
        '0':[' ']
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        l_result = []
        for c in itertools.product( *[self.dict_keys[d] for d in digits]):
            l_result.append("".join(c))
        return l_result
