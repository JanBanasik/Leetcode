class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        bobTravelledNodes = self.bobTravel(graph, bob)
        print(bobTravelledNodes)
        return self.aliceTravel(graph, amount, bobTravelledNodes)
    
    def bobTravel(self, graph, bob):
        
        queue = deque([bob])
        visited = set()
        parent = {}

        while queue:
            curr_node = queue.popleft()
            visited.add(curr_node)
            
            if curr_node == 0:
                break
            
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    parent[neighbor] = curr_node
                    queue.append(neighbor)
        
        
        path = []
        node = 0
        while node != bob:
            path.append(node)
            node = parent[node]
        path.append(bob)
        path.reverse() 
        
        bobTime = {}
        for time, node in enumerate(path):
            bobTime[node] = time
        return bobTime
    
    def aliceTravel(self, graph, amount, bobTravelledNodes):
        stack = [(0, 0, 0)] # node and current result and time
        visited = set()
        result = -float('inf')
        while stack:
            
            currNode, currSum, time = stack.pop()
            visited.add(currNode)
            price = amount[currNode]
            if currNode in bobTravelledNodes:
                if bobTravelledNodes[currNode] == time:
                    price = price // 2
                elif bobTravelledNodes[currNode] < time:
                    price = 0

            if len(graph[currNode]) == 1 and graph[currNode][0] in visited:
                result = max(result, currSum + price)
                
            else:
                for neighbor in graph[currNode]:
                    if neighbor not in visited:
                        stack.append((neighbor, currSum + price, time + 1))
        return result


