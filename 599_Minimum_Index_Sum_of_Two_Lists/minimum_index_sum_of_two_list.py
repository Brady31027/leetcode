class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans, common = collections.defaultdict(list), set(list1).intersection(set(list2))
        for k1, v1 in enumerate(list1):
            if v1 not in common: continue
            for k2, v2 in enumerate(list2):
                if v2 not in common or v2 != v1: continue
                ans[ k1 + k2 ].append(v1)
        return ans[min(ans)]
