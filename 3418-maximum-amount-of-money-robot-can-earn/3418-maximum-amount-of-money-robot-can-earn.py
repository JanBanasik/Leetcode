#
# @lc app=leetcode id=3418 lang=python3
#
# [3418] Maximum Amount of Money Robot Can Earn
#

# @lc code=start
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # problem is classical dp problem where we can use 2D dynamic programming to model both the position of the robot and the number of coins collected so far. We can define a dp array where dp[i][j] represents the maximum amount of money the robot can earn when it is at position i and has collected j coins. However we also need to take into account the number of "superpower" used -> that way dp will be mxnx3 where the last dimension represents the number of superpower used (0, 1 or 2).
        m, n = len(coins), len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]
        if dp[0][0][0] < 0:
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    self.calculate_new_max_values(dp, coins, i, j, k) 
        return max(dp[m-1][n-1])
    
    def calculate_new_max_values(self, dp, coins, i, j, k):
        if i == 0 and j == 0:
            return
        if i > 0:
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
            if coins[i][j] < 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
        
        if j > 0:
            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
            if coins[i][j] < 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        


# @lc code=end

