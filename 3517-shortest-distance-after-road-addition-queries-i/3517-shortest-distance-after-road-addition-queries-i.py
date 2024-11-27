class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(1, n):
            graph[i - 1] = [i]
        res = []
        for u, v in queries:
            graph[u].append(v)
            res.append(self.findShortestPath(graph, 0, n - 1))
        return res
    
    def findShortestPath(self, graph, start, stop):
        q = deque([(start, 0)])
        visited = set()
        while q:
            currNode, dist = q.popleft()
            visited.add(currNode)
            if currNode == stop:
                return dist
            else:
                for neighbor in graph[currNode]:
                    if neighbor not in visited:
                        q.append((neighbor, dist + 1))
        return -1