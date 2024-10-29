class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for i in range(m)]
        maxTravel: int = 0

        for j in range(1, n):
            foundGreaterPath = False
            for i in range(m):
                l_up = 0 if not( i > 0 and j > 0 and grid[i - 1][j - 1] < grid[i][j]) else dp[i - 1][j - 1] + 1
                l = 0 if not(j > 0 and grid[i][j - 1] < grid[i][j]) else dp[i][j - 1] + 1
                l_down = 0 if not( i < m - 1 and j > 0 and grid[i + 1][j - 1] < grid[i][j]) else dp[i + 1][j - 1] + 1
                dp[i][j] = max(dp[i][j], l_up, l, l_down)

                if dp[i][j] > maxTravel:
                    maxTravel = dp[i][j]
                    foundGreaterPath = True

            if not foundGreaterPath:
                break
        
        return maxTravel