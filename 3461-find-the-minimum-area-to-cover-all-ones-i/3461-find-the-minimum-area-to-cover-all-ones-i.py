class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_left, min_up, max_right, max_down = float('inf'), float('inf'), -1, -1

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    min_left = min(min_left, j)
                    min_up = min(min_up, i)
                    max_right = max(max_right, j)
                    max_down = max(max_down, i)
        
        return (max_right - min_left + 1) * (max_down - min_up + 1)