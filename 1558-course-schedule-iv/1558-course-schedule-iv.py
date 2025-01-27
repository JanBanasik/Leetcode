class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mat = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        res =  [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for a, b in prerequisites:
            mat[a][b] = True
            res[a][b] = True
            
        for node in range(numCourses):
            self.dfs(node, mat, res)
        
        for i in res:
            print(i)

        return [res[a][b] for a, b in queries]
    def dfs(self, node, mat, res):
        visited = set()
        stack = [node]
        while stack:
            currNode = stack.pop()
            visited.add(currNode)
            res[node][currNode] = True
            for neighbor in range(len(mat[currNode])):
                if mat[currNode][neighbor] and currNode != neighbor and (neighbor not in visited):
                    stack.append(neighbor)
        
