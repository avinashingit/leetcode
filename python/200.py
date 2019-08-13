class Solution:

    def dfs(self, grid, r, c, nr, nc):
        grid[r][c] = "0"
        if r-1 >= 0 and grid[r-1][c] == "1":
            self.dfs(grid, r-1, c, nr, nc)
        if r+1 < nr and grid[r+1][c] == "1":
            self.dfs(grid, r+1, c, nr, nc)
        if c-1 >= 0 and grid[r][c-1] == "1":
            self.dfs(grid, r, c-1, nr, nc)
        if c+1 < nc and grid[r][c+1] == "1":
            self.dfs(grid, r, c+1, nr, nc)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        total = 0
        nr, nc = len(grid), len(grid[0])
        # print(nr, nc)
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    total += 1
                    self.dfs(grid, i, j, nr, nc)
        return total
