class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        changes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        m, n = len(matrix), len(matrix[0])
        seen = [[False]*n for i in range(m)]
        total = 0
        i, j, di = 0, 0, 0
        while total < m*n:
            result.append(matrix[i][j])
            seen[i][j] = True
            ci = i + changes[di][0]
            cj = j + changes[di][1]
            if 0 <= ci < m and 0 <= cj < n and not seen[ci][cj]:
                i, j = ci, cj
            else:
                di = (di+1) % 4
                i, j = i + changes[di][0], j + changes[di][1]
            total += 1
        return result
