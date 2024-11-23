class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        newBox = [[-1 for _ in range(m)] for _ in range(n)]
        x = 0
        y = 0
        for row in reversed(box):
            for i in range(n):
                newBox[i][x] = row[i]
            x +=1 

        self.dropStones(newBox)
        return newBox
    
    def dropStones(self, newBox):
        m = len(newBox[0])
        n = len(newBox)
        for i in range(m):
            for j in range(n - 2, -1, -1):
                x = j
                y = i
                while x < n - 1 and newBox[x][y] == "#" and newBox[x+1][y] == ".":
                    newBox[x][y] = "."
                    newBox[x+1][y] = "#"
                    x +=1