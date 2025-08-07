class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for j in range(n)] for i in range(n)]
        dp[0] = matrix[0][:]

        for i in range(1,n):
            for j in range(n):
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j - 1] + matrix[i][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j + 1] + matrix[i][j])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
                
        return min(dp[-1])