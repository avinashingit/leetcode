from collections import defaultdict


class Solution:

    def checkwords(self, word1, word2, index):
        if word1 != "" and word2 != "":
            if index[word1[0]] == index[word2[0]]:
                self.checkwords(word1[1:], word2[1:], index)
            elif index[word1[0]] < index[word2[0]]:
                return True
            else:
                return False
        else:
            if word1 == "" and word2 != "":
                return True
            elif word1 != "" and word2 == "":
                return False
            else:
                return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = defaultdict(int)
        for i, char in enumerate(order):
            index[char] = i

        lwords = len(words)
        for i in range(lwords-1):
            if not self.checkwords(words[i], words[i+1], index):
                return False
        return True
