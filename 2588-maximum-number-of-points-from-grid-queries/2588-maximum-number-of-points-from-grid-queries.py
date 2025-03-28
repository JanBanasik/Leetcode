class Solution:
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sortedQueries = sorted(queries)
        m = len(grid)
        n = len(grid[0])
        results = self._bfs(grid, sortedQueries, m, n)
        h = {k : v for k, v in zip(sortedQueries, results)}
        
        return [h.get(x, results[-1]) for x in queries]
    
    def _bfs(self, grid, queries, m, n):
        indexQuery = 0
        result = [0]
        visited = set()
        visited.add((0, 0))
        q = [(grid[0][0], (0, 0))]
        heapq.heapify(q)
        flagToBreak = False
        while q and indexQuery < len(queries):
            
            while q[0][0] >= queries[indexQuery]:
                if indexQuery == len(queries) - 1:
                    flagToBreak = True
                    break
                indexQuery +=1
                result.append(result[-1])
            if flagToBreak:
                break
            (_, (x, y)) = heapq.heappop(q)
            
            result[-1] +=1

            for dx, dy in self.directions:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < m) and (0 <= ny < n) and (nx, ny) not in visited:
                    heapq.heappush(q, (grid[nx][ny], (nx, ny)))
                    visited.add((nx, ny))
        return result