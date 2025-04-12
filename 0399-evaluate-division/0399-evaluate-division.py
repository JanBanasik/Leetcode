def dfs(source, destination, graph, visited):
    if source not in graph or destination not in graph:
        return -1
    if source == destination:
        return 1
    
    visited.add(source)
    for neighbor, value in graph[source].items():
        if neighbor not in visited:
            result = dfs(neighbor, destination, graph, visited)
            if result != -1:
                return result * value
    return -1
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (num, denum), val in zip(equations, values):
            if num not in graph:
                graph[num] = {}
            if denum not in graph:
                graph[denum] = {}
            graph[num][denum] = val
            graph[denum][num] = 1 / val
        ans = []
        for query in queries:
            ans.append(dfs(query[0], query[1], graph, set()))
        return ans