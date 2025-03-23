import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        mod = 1_000_000_007
        
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        pq = [(0, 0)]
        heapq.heapify(pq)
        dist = [float('inf') for _ in range(n)]
        pathCount = [0 for _ in range(n)]
        pathCount[0] = 1
        
        while pq:
            
            currTime, currNode = heapq.heappop(pq)
            
            if currTime > dist[currNode]:
                continue

            for neighbor, time in graph[currNode]:
                if currTime + time < dist[neighbor]:
                    dist[neighbor] = currTime + time
                    pathCount[neighbor] = pathCount[currNode]
                    heapq.heappush(pq, (dist[neighbor], neighbor))
                
                elif currTime + time == dist[neighbor]:
                    pathCount[neighbor] = (pathCount[neighbor] + pathCount[currNode]) % mod
        return pathCount[n - 1]
