class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)
    
    def bfs(self, grid):
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m = len(grid) ; n = len(grid[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        q = []
        heapq.heappush(q, (0, (0, 0)))
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        while q:
            currDist, (x, y) = heapq.heappop(q)
            
            if x == m - 1 and y == n - 1:
                return currDist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if dist[nx][ny] != float('inf'):
                        continue

                    if currDist + 1 >= grid[nx][ny]:
                        newTime = currDist + 1
                    else:
                        diff = abs(grid[nx][ny] - currDist)
                        if diff % 2 == 1:
                            newTime = grid[nx][ny]
                        else:
                            newTime = grid[nx][ny] + 1
                    
                    if newTime < dist[nx][ny]:
                        dist[nx][ny] = newTime
                        heapq.heappush(q, (newTime, (nx, ny)))
        

        return -1