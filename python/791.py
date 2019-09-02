from collections import Counter
import heapq


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = {x: i for i, x in enumerate(list(S))}
        heap = []
        for char in T:
            heapq.heappush(heap, (order.get(char, 27), char))
        result = ""
        while len(heap):
            _, c = heapq.heappop(heap)
            result += c
        return result

#######################


class Solution2:
    def customSortString(self, S: str, T: str) -> str:
        counts = Counter(T)
        result = ""
        for c in S:
            if c in counts:
                result += ''.join([c]*counts[c])
                counts[c] = 0
        for c in counts:
            result += ''.join([c]*counts[c])

        return result
