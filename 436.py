# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        l_ans, interval_size = [], len(intervals)
        l_sorted_intervals = sorted([(v.start, i) for i, v in enumerate(intervals)])
        for interval in intervals:
            idx = bisect.bisect_right(l_sorted_intervals, (interval.end,))
            l_ans.append(l_sorted_intervals[idx][1] if idx < interval_size else -1)
        return l_ans
