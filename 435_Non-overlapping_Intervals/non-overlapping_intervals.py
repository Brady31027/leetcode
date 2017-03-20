# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        size = len(intervals)
        if size < 2: return 0
        remove_cnt, prev_tail = 0, 0
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[prev_tail].end:
                if intervals[i].end < intervals[prev_tail].end: prev_tail = i
                remove_cnt += 1
            else:
                prev_tail = i
        return remove_cnt
        
