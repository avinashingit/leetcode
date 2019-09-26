class Solution(object):

    def dfs(self, board, r, c, m, n, word):

        if not word:
            return True

        if r >= m or r < 0 or c >= n or c < 0:
            return False

        if board[r][c] != word[0]:
            return False

        temp = board[r][c]
        board[r][c] = '#'

        if self.dfs(board, r+1, c, m, n, word[1:]) or self.dfs(board, r-1, c, m, n, word[1:]) or self.dfs(board, r, c+1, m, n, word[1:]) or self.dfs(board, r, c-1, m, n, word[1:]):
            return True

        board[r][c] = temp

        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False

        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if self.dfs(board, r, c, m, n, word):
                    return True
        return False
        
