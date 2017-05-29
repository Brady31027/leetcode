class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tbl1 = {v: k for k, v in enumerate(list1) }
        minimal, ans = 1e9, []
        for k, v in enumerate(list2):
            i = tbl1.get(v, 1e9)
            if i + k < minimal:
                minimal = i + k
                ans = [v]
            elif i + k == minimal:
                ans.append(v)
        return ans
