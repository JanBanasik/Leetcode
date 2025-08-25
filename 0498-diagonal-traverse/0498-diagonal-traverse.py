class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        startX, startY = 0, 0
        up = True
        result = []
        
        for _ in range(m + n - 1):
            startX, startY = self.addValues(startX, startY, result, up, m, n, mat)
            startX, startY = self.moveCoords(startX, startY, up, m, n)
            up = not up
        return result    
    
    def addValues(self, x, y, result, up, m, n, mat):

        dx, dy = (-1, 1) if up else (1, -1)
        while 0 <= x < m and 0 <= y < n:
            result.append(mat[x][y])
            x, y = x + dx, y + dy
        
        x -=dx; y-=dy
        return x, y
    
    def moveCoords(self, x, y, up, m, n):
        if up:
            return (x, y+1) if y < n-1 else (x+1, y)
        else:
            return (x+1, y) if x < m-1 else (x, y+1)


        

