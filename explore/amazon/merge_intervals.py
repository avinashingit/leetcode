class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x: x[0])
        if not intervals:
            return intervals
        result.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                temp = result.pop()
                result.append([temp[0], max(temp[1], interval[1])])
        return result
