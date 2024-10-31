class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda x: x[0])
        pos = []
        for i in factory:
            for _ in range(i[1]):
                pos.append(i[0])
        cost = 0
        m = len(robot)
        n = len(pos)
        dp = [[0 for _ in range(n + 1)] for i in range(m + 1)]

        for i in range(m):
            dp[i][n] = float('inf')
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                assign = abs(robot[i] - pos[j]) + dp[i + 1][j + 1]
                skip = dp[i][j + 1]
                dp[i][j] = min(assign, skip)
        return dp[0][0]