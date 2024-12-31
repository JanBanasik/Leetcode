class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for i in range(days[-1] + 1)]
        dp[0] = 0
        daysSet = set(days)
        for i in range(1, len(dp)):
            if i in daysSet:
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[i - 7] + costs[1] if i >= 7 else costs[1]
                cost30 = dp[i - 30] + costs[2] if i >= 30 else costs[2]
                dp[i] = min(cost1, cost7, cost30)
            else:
                dp[i] = dp[i-1]
        return dp[-1]