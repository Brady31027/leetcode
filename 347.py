class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_ans = {}
        set_nums = set(nums)
        for s in set_nums:
            if len(dict_ans) < k:
                dict_ans[s] = nums.count(s)
            else:
                cur_count = nums.count(s)
                min_value = min(dict_ans.values())
                if cur_count > min_value:
                    dict_ans[s] = cur_count
                    min_idx = dict_ans.keys()[dict_ans.values().index(min_value)]
                    del dict_ans[min_idx]
        return list(dict_ans.keys())
        
