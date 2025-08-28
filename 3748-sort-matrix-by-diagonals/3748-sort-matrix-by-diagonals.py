class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n: int = len(grid)

        self.sortLowerDiagonals(grid, n)
        self.sortUpperDiagonals(grid, n)
        
        return grid
    
    def sortLowerDiagonals(self, grid, n):

        for diag_length, startX, startY in zip(range(n, 0, -1), range(0, n), [0] * n):
            x, y = startX, startY
            values = []
            for _ in range(diag_length):
                values.append(grid[x][y])
                x +=1
                y +=1
            values.sort(reverse=True)
            x, y = startX, startY
            for index in range(diag_length):
                grid[x][y] = values[index]
                x +=1
                y +=1
        
    
    def sortUpperDiagonals(self, grid, n):

        for diag_length, startX, startY in zip(range(n - 1, 1, -1), [0] * (n - 1), range(1, n)):
            x, y = startX, startY
            values = []
            for _ in range(diag_length):
                values.append(grid[x][y])
                x +=1
                y +=1
            values.sort(reverse=False)

            x, y = startX, startY
            for index in range(diag_length):
                grid[x][y] = values[index]
                x +=1
                y +=1
        

    