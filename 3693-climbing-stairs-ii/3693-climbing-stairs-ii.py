class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + 4, n + 1)):
                dp[j] = min(
                    dp[j],
                    dp[i] + costs[j - 1] + (j - i) ** 2
                )

        return dp[n]