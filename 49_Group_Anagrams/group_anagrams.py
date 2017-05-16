ass Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = collections.defaultdict(list)
        ans = []
        
        def getKey(s):
            return "".join(sorted(s))
            
        for st in strs:
            key = getKey(st)
            memo[key].append(st)
            
        for hashEntry in memo:
            ans.append( memo[hashEntry] )
        
        return ans
