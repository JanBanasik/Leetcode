


class Solution:

    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col
        
        def __lt__(self, other):
            return self.height < other.height

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        pq = []
        for i in range(m):
            heapq.heappush(pq, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(pq, self.Cell(heightMap[i][n - 1], i, n - 1))
            visited[i][0] = visited[i][n - 1] = True
        
        for i in range(n):
            heapq.heappush(pq, self.Cell(heightMap[0][i], 0, i))
            heapq.heappush(pq, self.Cell(heightMap[m - 1][i], m - 1, i))
            visited[0][i] = visited[m - 1][i] = True
        
        result = 0
        while pq:
            currCell = heapq.heappop(pq)
            currRow = currCell.row
            currCol = currCell.col
            minBoundaryHeight = currCell.height

            for dx, dy in self.directions:
                nr = currRow + dx
                nc = currCol + dy
                if (self.is_valid_cell(nr, nc, m, n) and not visited[nr][nc]):
                    nHeight = heightMap[nr][nc]
                    if nHeight < minBoundaryHeight:
                        result += (minBoundaryHeight - nHeight)

                    heapq.heappush(pq, self.Cell(max(nHeight, minBoundaryHeight), nr, nc))
                    visited[nr][nc] = True
        return result

    
    def is_valid_cell(self, row, col, m, n):
        return (0 <= row < m) and (0 <= col < n) 