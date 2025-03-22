class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        degrees = [0 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] +=1
            degrees[v] +=1
        # for a group of n each degree should be:
        # lenNodes - 1

        visited = [False for _ in range(n)]

        connectedComponents = 0
        for node in range(n):
            if not visited[node]:
                nodesInGroup = self._dfs(graph, node, visited)
                if all(degrees[x] == len(nodesInGroup) - 1 for x in nodesInGroup):
                    connectedComponents +=1
        return connectedComponents
    
    def _dfs(self, graph, node, visited):
        stack = [node]
        componentNodes = set()
        while stack:
            currNode = stack.pop(-1)
            visited[currNode] = True
            componentNodes.add(currNode)
            for neighbor in graph[currNode]:
                if neighbor not in componentNodes:
                    stack.append(neighbor)
        
        return list(componentNodes)