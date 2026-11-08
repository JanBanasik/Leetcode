class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        row_count: list[int] = [0] * m
        col_count: list[int] = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        counter: int = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    counter += 1
        return counter
                