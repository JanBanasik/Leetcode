class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    left = dp[i][j - 1] if j > 0 else 0
                    left_up = dp[i - 1][j - 1] if (i > 0 and j > 0) else 0
                    up = dp[i - 1][j] if i > 0 else 0
                    if left == up == left_up:
                        dp[i][j] = left + 1
                    else:
                        dp[i][j] = min(up, left, left_up) + 1
        
        return sum([sum(x) for x in dp])
        