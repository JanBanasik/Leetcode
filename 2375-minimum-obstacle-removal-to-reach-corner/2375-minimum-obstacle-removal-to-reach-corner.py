class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        return self.zero_one_bfs(grid)
    
    def zero_one_bfs(self, grid):
        m = len(grid)
        n = len(grid[0])
        newGrid = [[float('inf') for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dq = deque()
        dq.append((0, 0))
        newGrid[0][0] = grid[0][0]
        while dq:
            x, y = dq.popleft()

            for a, b in directions:
                if x + a >= m or x + a < 0 or y + b >= n or y + b < 0:
                    continue
                newCost = newGrid[x][y] + grid[x + a][y + b]
                if newCost < newGrid[x + a][y + b]:
                    newGrid[x + a][y + b] = newCost
                    if grid[x + a][y + b] == 0:
                        dq.appendleft((x+a,y+b))
                    else:
                        dq.append((x+a,y+b))
        return newGrid[m - 1][n - 1] 