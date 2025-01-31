class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    labelIndex = 0
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        countOnes = 0
        countZeros = 0
        labeledIslands = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                countOnes += grid[i][j]
                countZeros += not grid[i][j]
        if countZeros == 0:
            return n * n
        if countOnes == 0:
            return 1
         
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.fillIsland(grid, mat, i, j, n, labeledIslands)

        result = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    result = max(result, self.connectFourIslands(mat, i, j, n, labeledIslands))
        return result

    def fillIsland(self, grid, mat, i, j, n, labeledIslands):
        stack = [(i, j)]
        visited = set()
        visited.add((i, j))
        islandSize = 0
        while stack:
            currX, currY = stack.pop(-1)
            grid[currX][currY] = -1
            islandSize += 1
            for dx, dy in self.directions:
                nx = currX + dx
                ny = currY + dy
                if (0 <= nx < n) and (0 <= ny < n) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
        
        for (a,b) in visited:
            mat[a][b] = islandSize
            labeledIslands[a][b] = self.labelIndex
        self.labelIndex +=1
    
    def connectFourIslands(self, mat, i, j, n, labeledIslands):
        newIslandSize = 0
        flag = False
        labels = {}
        for dx, dy in self.directions:
            nx = i + dx
            ny = j + dy

            if (0 <= nx < n) and (0 <= ny < n) and mat[nx][ny] > 0:
                labels[labeledIslands[nx][ny]] = mat[nx][ny]

        res = 0
        for key, value in labels.items():
            res += value
        return res + 1