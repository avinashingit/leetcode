from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not (wordList and beginWord) or endWord not in wordList:
            return 0
        combinations = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                combinations[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord:True}

        while queue:
            el, count = queue.popleft()
            for i in range(len(el)):
                pattern = el[:i] + "*" + el[i+1:]
                for word in combinations[pattern]:
                    if word == endWord:
                        return count + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, count+1))
        return 0
