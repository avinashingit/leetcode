import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])
        heap, count = [], 1
        heapq.heappush(heap, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] < heap[0]:
                count += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return count
                
