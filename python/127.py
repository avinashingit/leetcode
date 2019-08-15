from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or (endWord not in wordList) or (beginWord is endWord):
            return 0
        combinations = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                combinations[word[:j]+"*"+word[j+1:]].append(word)
        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord: True}
        while queue:
            word, count = queue.popleft()
            for i in range(len(word)):
                iword = word[:i] + "*" + word[i+1:]
                for xword in combinations[iword]:
                    if xword == endWord:
                        return count + 1
                    if xword not in visited:
                        visited[xword] = True
                        queue.append((xword, count+1))
                # combinations[iword] = []
        return 0
