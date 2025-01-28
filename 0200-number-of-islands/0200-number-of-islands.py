class Solution:

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        numberOfIslands: int = 0
        m: int = len(grid)
        n: int = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    numberOfIslands +=1
                    self.fillIslands(grid, i, j, m, n)
        return numberOfIslands
    
    def fillIslands(self, grid, i, j, m, n):
        stack = [(i, j)]
        visited = set()
        while stack:
            currX, currY = stack.pop(-1)
            grid[currX][currY] = "#"
            for dx, dy in self.directions:
                nx = currX + dx
                ny = currY + dy
                if (0 <= nx < m) and (0 <= ny < n) and (nx, ny) not in visited and grid[nx][ny] == "1":
                    stack.append((nx, ny))
        