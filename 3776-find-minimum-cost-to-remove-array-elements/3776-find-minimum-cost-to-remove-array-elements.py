class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [[float('inf')] * (n + 2) for _ in range(n)]

        for i in range(n):
            dp[i][n] = nums[i]
            dp[i][n + 1] = nums[i]
        for i in range(n - 1):
            dp[i][n - 1] = max(nums[i], nums[n - 1])
        
        for j in range(n - 2, 0, -1):
            for i in range(j):
                c1 = max(nums[i], nums[j]) + dp[j + 1][j + 2]
                c2 = max(nums[i], nums[j + 1]) + dp[j][j + 2]
                c3 = max(nums[j], nums[j + 1]) + dp[i][j + 2]
                dp[i][j] = min(c1,c2,c3)
        
        c1 = max(nums[0], nums[1]) + dp[2][3]
        c2 = max(nums[0], nums[2]) + dp[1][3]
        c3 = max(nums[1], nums[2]) + dp[0][3]
        return min(c1, c2,c3)
          
                