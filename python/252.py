class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i, interval in enumerate(intervals):
            if i != 0:
                if interval[0] < intervals[i-1][1]:
                    return False
        return True
