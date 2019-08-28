class Solution:

    def dfs(self, board, word, r, c, nr, nc):
        if len(word) == 0:
            return True
        if (r < 0) or (r >= nr) or (c < 0) or (c >= nc) or (board[r][c] != word[0]):
            return False
        temp = board[r][c]
        board[r][c] = '#'
        result = False
        if self.dfs(board, word[1:], r+1, c, nr, nc) or self.dfs(board, word[1:], r-1, c, nr, nc) or \
                self.dfs(board, word[1:], r, c-1, nr, nc) or self.dfs(board, word[1:], r, c+1, nr, nc):
            result = True
        board[r][c] = temp
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        nr, nc = len(board), len(board[0])
        for i in range(nr):
            for j in range(nc):
                if self.dfs(board, word, i, j, nr, nc):
                    return True
        return False
