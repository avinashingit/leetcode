from collections import defaultdict


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        indices = defaultdict(int)
        for i, b in enumerate(B):
            indices[b] = i
        result = []
        for i, a in enumerate(A):
            result.append(indices[a])
        return result
