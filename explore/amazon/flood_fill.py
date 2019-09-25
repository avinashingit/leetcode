class Solution(object):

    def dfs(self, image, r, c, m, n, color, newColor):
        image[r][c] = '#'
        if r+1 < m and image[r+1][c] == color:
            self.dfs(image, r+1, c, m, n, color, newColor)
        if r-1 >= 0 and image[r-1][c] == color:
            self.dfs(image, r-1, c, m, n, color, newColor)
        if c+1 < n and image[r][c+1] == color:
            self.dfs(image, r, c+1, m, n, color, newColor)
        if c-1>=0 and image[r][c-1] == color:
            self.dfs(image, r, c-1, m, n, color, newColor)
        image[r][c] = newColor

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.dfs(image, sr, sc, len(image), len(image[0]), image[sr][sc], newColor)
        return image
        
