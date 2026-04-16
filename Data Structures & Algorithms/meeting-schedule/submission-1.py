"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Just check to see if (end of i > start of i+1)
        intervals.sort(key=lambda i: i.start)
        for i, interval in enumerate(intervals):
            if i + 1 < len(intervals) and intervals[i].end > intervals[i + 1].start:
                return False
        return True
