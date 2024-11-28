class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        return self.zero_one_bfs(grid)
    
    def zero_one_bfs(self, grid):
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dq = deque()
        dq.append((0, 0))
        dist[0][0] = grid[0][0]
        
        while dq:
            x, y = dq.popleft()
            if x == m - 1 and y == n - 1:
                return dist[m - 1][n - 1]
            for a, b in directions:
                nx, ny = x + a, y + b
                if (0 <= nx < m) and (0 <= ny < n):
                    newCost = dist[x][y] + grid[nx][ny]
                    if newCost < dist[nx][ny]:
                        dist[nx][ny] = newCost
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx,ny))
                        else:
                            dq.append((nx,ny))

        