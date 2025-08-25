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
    
    def addValues(self, startX, startY, result, up, m, n, mat):

        dx, dy = (-1, 1) if up else (1, -1)
        while True:
            result.append(mat[startX][startY])
            if (0<=(nx:=startX+dx)<m) and (0<=(ny:=startY+dy)<n):
                startX = nx; startY=ny
            else:
                break
        return startX, startY
    
    def moveCoords(self, x, y, up, m, n):
        if up:
            return (x, y+1) if y < n-1 else (x+1, y)
        else:
            return (x+1, y) if x < m-1 else (x, y+1)


        

