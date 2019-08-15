class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = -1, -1
        minDistance = len(words)
        for i, word in enumerate(words):
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                minDistance = min(minDistance, abs(p2-p1))
        return minDistance
